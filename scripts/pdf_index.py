"""Join the per-file PDFs into one, with a linked index and bookmarks.

Called by make_pdf.sh as:  python3 scripts/pdf_index.py <parts.tsv> <out.pdf>

parts.tsv has one line per solution file, in PDF order:
    <source .py path> TAB <its pdf> [TAB <its screenshot page pdf>]

The output starts with an index (site > section > lesson > problem, with page
numbers). Every problem in it is a link to its first page, and the same tree is
added as PDF bookmarks (the table of contents in phone PDF viewers). Only
poppler (pdfinfo, pdftotext, pdfunite), enscript and Ghostscript are needed.
"""
import html
import os
import re
import subprocess
import sys
import tempfile
from collections import OrderedDict

NEETCODE = "Data Structures & Algorithms"
SITES = OrderedDict([(NEETCODE, "NeetCode"), ("codility", "Codility")])
WIDTH = 76                      # characters per index line (Courier 10 on A4)


def run(*cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw).stdout


def page_count(pdf):
    return int(re.search(r"Pages:\s+(\d+)", run("pdfinfo", pdf)).group(1))


def title(path):
    """NeetCode: the docstring title ('Max Consecutive Ones'). Codility / no title: the folder name."""
    if os.path.basename(path) == "cheatsheet.py":
        return "Cheatsheet"
    folder = os.path.basename(os.path.dirname(path))
    if path.startswith("codility/"):           # docstring titles there are CamelCase
        return re.sub(r"[-_]+", " ", folder).title()
    with open(path, encoding="utf-8") as f:
        head = f.read(400)
    m = re.match(r'r?"""\s*\n(.+?) \((?:NeetCode|Codility)\)', head)
    if m:
        return m.group(1).strip()
    return re.sub(r"[-_]+", " ", folder).title()


def build_tree(rows, first_page):
    """site -> section -> lesson ('' if none) -> [(title, page)], one entry per problem."""
    tree = OrderedDict()
    seen = set()
    for (src, *_), page in zip(rows, first_page):
        parts = src.split("/")
        site = parts[0]
        rest = parts[1:]                       # section/[lesson/]problem/file  or  section/cheatsheet.py
        section = rest[0]
        if rest[-1] == "cheatsheet.py":
            lesson, key = "", (site, section, "cheatsheet")
        elif len(rest) == 4:
            lesson, key = rest[1], (site, section, rest[1], rest[2])
        else:
            lesson, key = "", (site, section, rest[1])
        if key in seen:                        # extra approach of the same problem
            continue
        seen.add(key)
        tree.setdefault(site, OrderedDict()).setdefault(section, OrderedDict()) \
            .setdefault(lesson, []).append((title(src), page))
    return tree


def index_lines(tree):
    """[(text, target page or None)] for the index pages."""
    lines = []
    for site, sections in tree.items():
        lines += [(SITES.get(site, site).upper(), None), ("", None)]
        for section, lessons in sections.items():
            lines.append((section, None))
            for lesson, problems in lessons.items():
                indent = "    "
                if lesson:
                    lines.append(("  " + lesson, None))
                    indent = "      "
                for name, page in problems:
                    left = indent + name + " "
                    right = " " + str(page)
                    lines.append((left + "." * max(2, WIDTH - len(left) - len(right)) + right, page))
            lines.append(("", None))
    return lines


def render_index(lines, out_pdf, tmp):
    txt = os.path.join(tmp, "index.txt")
    with open(txt, "w", encoding="utf-8") as f:
        f.write("INDEX  (tap a problem to jump to it)\n\n")
        f.write("\n".join(text for text, _ in lines) + "\n")
    ps = os.path.join(tmp, "index.ps")
    run("enscript", "-q", "-fCourier10", "--header=Index||Page $% of $=", "-p", ps, txt)
    run("ps2pdf", ps, out_pdf)
    return page_count(out_pdf)


def link_rects(index_pdf, lines):
    """Find each entry line on the index pages: [(index page, x0, y0, x1, y1, target)]."""
    xml = run("pdftotext", "-bbox-layout", index_pdf, "-")
    targets = [(re.sub(r"\s+", " ", text).strip(), page) for text, page in lines if page]
    rects, t = [], 0
    for pno, page_xml in enumerate(re.findall(r"<page (.*?)</page>", xml, re.S), start=1):
        height = float(re.search(r'height="([\d.]+)"', page_xml).group(1))
        for line in re.findall(r"<line (.*?)</line>", page_xml, re.S):
            words = [html.unescape(w) for w in re.findall(r">([^<]*)</word>", line)]
            if t < len(targets) and " ".join(words) == targets[t][0]:
                x0, y0, x1, y1 = (float(v) for v in re.match(
                    r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)"', line).groups())
                rects.append((pno, x0, height - y1, x1, height - y0, targets[t][1]))
                t += 1
    if t != len(targets):
        sys.exit(f"pdf_index: linked {t} of {len(targets)} index entries; index layout changed?")
    return rects


def ps_string(s):
    return "(" + s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)") + ")"


def pdfmarks(rects, tree):
    out = []
    for pno, x0, y0, x1, y1, page in rects:
        out.append(f"[ /SrcPg {pno} /Rect [{x0:.1f} {y0 - 1:.1f} {x1:.1f} {y1 + 1:.1f}] "
                   f"/Border [0 0 0] /Page {page} /View [/XYZ null null null] "
                   f"/Subtype /Link /ANN pdfmark")

    # Bookmarks: Index, then site > section > lesson > problem (closed by default)
    out.append(f"[ /Title {ps_string('Index')} /Page 1 /OUT pdfmark")
    for site, sections in tree.items():
        out.append(f"[ /Count -{len(sections)} /Title {ps_string(SITES.get(site, site))} "
                   f"/Page {first(sections)} /OUT pdfmark")
        for section, lessons in sections.items():
            named = [l for l in lessons if l]
            loose = lessons.get("", [])
            out.append(f"[ /Count -{len(named) + len(loose)} /Title {ps_string(section)} "
                       f"/Page {first(lessons)} /OUT pdfmark")
            for name, page in loose:
                out.append(f"[ /Title {ps_string(name)} /Page {page} /OUT pdfmark")
            for lesson in named:
                problems = lessons[lesson]
                out.append(f"[ /Count -{len(problems)} /Title {ps_string(lesson)} "
                           f"/Page {problems[0][1]} /OUT pdfmark")
                for name, page in problems:
                    out.append(f"[ /Title {ps_string(name)} /Page {page} /OUT pdfmark")
    out.append("[ /PageMode /UseOutlines /DOCVIEW pdfmark")
    return "\n".join(out) + "\n"


def first(d):
    """Lowest page number anywhere under d."""
    if isinstance(d, list):
        return min(p for _, p in d)
    return min(first(v) for v in d.values())


def main():
    manifest, out = sys.argv[1], sys.argv[2]
    rows = [line.rstrip("\n").split("\t") for line in open(manifest, encoding="utf-8") if line.strip()]
    pdfs = [p for row in rows for p in row[1:]]
    counts = {p: page_count(p) for p in pdfs}

    with tempfile.TemporaryDirectory() as tmp:
        index_pdf = os.path.join(tmp, "index.pdf")

        def layout(index_pages):
            first_page, page = [], index_pages + 1
            for row in rows:
                first_page.append(page)
                page += sum(counts[p] for p in row[1:])
            tree = build_tree(rows, first_page)
            return tree, index_lines(tree)

        # The index length depends on nothing but the entries, so one dry render
        # tells us how many pages it takes; then render it with real page numbers.
        tree, lines = layout(1)
        index_pages = render_index(lines, index_pdf, tmp)
        tree, lines = layout(index_pages)
        if render_index(lines, index_pdf, tmp) != index_pages:
            sys.exit("pdf_index: index length changed between passes")

        merged = os.path.join(tmp, "merged.pdf")
        run("pdfunite", index_pdf, *pdfs, merged)

        marks = os.path.join(tmp, "marks.ps")
        with open(marks, "w", encoding="utf-8") as f:
            f.write(pdfmarks(link_rects(index_pdf, lines), tree))
        run("gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=pdfwrite",
            f"-sOutputFile={out}", merged, marks)

    links = sum(1 for _, p in lines if p)
    print(f"index: {index_pages} page(s), {links} linked problems")


if __name__ == "__main__":
    main()

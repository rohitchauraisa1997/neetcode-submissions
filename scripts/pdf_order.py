"""Print the .py files in PDF order: all NeetCode problems first, then Codility.

NeetCode follows the course: sections and lessons in their numbered order (see
organize.py), each section's cheatsheet.py first. Within a lesson (and for
Codility), problems are ordered by the first commit that added any of their
files. Inside a problem folder, the file holding the full question comes first,
then the other approaches in commit order. Renamed or moved files, committed or
not, are traced back to their original commit.
"""
import os
import runpy
import subprocess

# Paths below are relative to the repo root.
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

NEETCODE = "Data Structures & Algorithms"
CODILITY = "codility"
CHEATSHEET = "cheatsheet.py"


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


commit_index = {h: i for i, h in enumerate(git("rev-list", "--reverse", "HEAD").split())}

def pair_renames(added, deleted):
    """Pair renamed files by content: {new path: old path}.

    Adding a question to a short file makes it too different for git's rename
    detection, so match on content instead: the new file ends with the old file's
    text. A file that was also edited falls back to the only deleted file left in
    its folder.
    """
    pairs = {}
    deleted = dict(deleted)
    unmatched = []
    for new, new_text in added.items():
        match = next((old for old, text in deleted.items()
                      if os.path.dirname(old) == os.path.dirname(new) and new_text.endswith(text)), None)
        if match:
            pairs[new] = match
            del deleted[match]
        else:
            unmatched.append(new)
    for new in unmatched:
        same_dir = [old for old in deleted if os.path.dirname(old) == os.path.dirname(new)]
        if len(same_dir) == 1:
            pairs[new] = same_dir[0]
            del deleted[same_dir[0]]
    return pairs


def py_paths(out):
    return [p for p in out.split("\0") if p.endswith(".py")]


# Renames in the working tree that aren't committed yet: {new path: path at HEAD}.
staged = {}
for line in git("diff", "--cached", "-M20%", "HEAD", "--name-status").splitlines():
    parts = line.split("\t")
    if parts[0].startswith("R"):
        staged[parts[2]] = parts[1]
wt_added = {}
for new in py_paths(git("ls-files", "-z", "--others", "--exclude-standard")):
    with open(new, encoding="utf-8") as f:
        wt_added[new] = f.read()
wt_deleted = {old: git("show", f"HEAD:{old}")
              for old in py_paths(git("diff", "HEAD", "--name-only", "--diff-filter=D", "-z"))
              if old not in staged.values()}
pending = {**staged, **pair_renames(wt_added, wt_deleted)}


def renamed_in(commit, path):
    """If `commit` created `path` by renaming another file, return that file's old path."""
    parents = git("rev-list", "--parents", "-n1", commit).split()[1:]
    if not parents:
        return None
    folder = os.path.dirname(path)
    status = git("show", "--no-renames", "--name-status", "--format=", "-z", commit, "--", folder).split("\0")
    added, deleted = {}, {}
    for kind, p in zip(status[::2], status[1::2]):
        if p.endswith(".py") and kind == "A":
            added[p] = git("show", f"{commit}:{p}")
        elif p.endswith(".py") and kind == "D":
            deleted[p] = git("show", f"{parents[0]}:{p}")
    return pair_renames(added, deleted).get(path)


def first_commit(path):
    path, rev = pending.get(path, path), "HEAD"
    while True:
        out = git("log", "--follow", "--name-only", "--format=@%H", rev, "--", path)
        entries = [e.split() for e in out.split("@")[1:]]
        if not entries:
            return len(commit_index)
        commit = entries[-1][0]
        name = out.split("@")[-1].split("\n", 1)[1].strip()  # the file's name in that commit
        old = renamed_in(commit, name)
        if old is None:
            return commit_index[commit]
        path, rev = old, f"{commit}^"


def has_full_question(path):
    with open(path, encoding="utf-8") as f:
        head = f.read(300)
    return "another approach" not in head


def py_files(d):
    return [os.path.join(d, f) for f in os.listdir(d) if f.endswith(".py") and f != CHEATSHEET]


def subdirs(d):
    return sorted(os.path.join(d, x) for x in os.listdir(d) if os.path.isdir(os.path.join(d, x)))


def print_problems(folders):
    """Problem folders by first commit; question file first inside each."""
    problems = []
    for d in folders:
        files = py_files(d)
        if files:
            ranked = sorted(files, key=lambda p: (not has_full_question(p), first_commit(p), p))
            problems.append((min(first_commit(p) for p in files), ranked))
    for _, files in sorted(problems):
        for p in files:
            print(p)


# Lesson order comes from the course map (folder names sort the same way, but
# this also handles a section with 10+ lessons).
lesson_dirs = runpy.run_path("scripts/organize.py")["LESSON_DIR"].values()
lesson_rank = {d: i for i, d in enumerate(lesson_dirs)}

# NeetCode: section -> (cheatsheet) -> lesson -> problem. A section without
# lessons (e.g. 13 Sliding Window) holds problem folders directly.
for section in subdirs(NEETCODE):
    if os.path.exists(os.path.join(section, CHEATSHEET)):
        print(os.path.join(section, CHEATSHEET))
    direct = [d for d in subdirs(section) if py_files(d)]
    print_problems(direct)
    lessons = [d for d in subdirs(section) if d not in direct]
    for lesson in sorted(lessons, key=lambda d: (lesson_rank.get(d, len(lesson_rank)), d)):
        print_problems(subdirs(lesson))

# Codility: lesson folders are numbered as on the site, so they sort by name.
for lesson in subdirs(CODILITY):
    print_problems(subdirs(lesson))

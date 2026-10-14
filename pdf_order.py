"""Print the .py files in commit order: all NeetCode problems first, then Codility.

Problems are ordered by the first commit that added any of their files. Inside a
problem folder, the file holding the full question comes first, then the other
approaches in commit order. Files renamed but not yet committed are traced back to
their old path.
"""
import os
import subprocess

TOPICS = ["Data Structures & Algorithms", "codilty"]


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


commit_index = {h: i for i, h in enumerate(git("rev-list", "--reverse", "HEAD").split())}

# new path -> old path, for renames not yet committed. Matched by content (the
# renamed file ends with the old file's text) so it works whether or not the
# renames are staged.
pending = {}
for line in git("diff", "--cached", "-M20%", "HEAD", "--name-status").splitlines():
    parts = line.split("\t")
    if parts[0].startswith("R"):
        pending[parts[2]] = parts[1]

deleted = [p for p in git("diff", "HEAD", "--name-only", "--diff-filter=D", "-z").split("\0")
           if p.endswith(".py") and p not in pending.values()]
added = [p for p in git("ls-files", "-z", "--others", "--exclude-standard").split("\0") if p.endswith(".py")]
old_text = {p: git("show", f"HEAD:{p}") for p in deleted}
unmatched = []
for new in added:
    with open(new, encoding="utf-8") as f:
        new_text = f.read()
    match = next((old for old, text in old_text.items()
                  if os.path.dirname(old) == os.path.dirname(new) and new_text.endswith(text)), None)
    if match:
        pending[new] = old_text.pop(match) and match
    else:
        unmatched.append(new)
# Content differs (file was also edited): fall back to the only deleted file left in that folder.
for new in unmatched:
    same_dir = [old for old in old_text if os.path.dirname(old) == os.path.dirname(new)]
    if len(same_dir) == 1:
        pending[new] = same_dir[0]
        del old_text[same_dir[0]]


def first_commit(path):
    path = pending.get(path, path)
    hashes = git("log", "--follow", "--format=%H", "--", path).split()
    return commit_index.get(hashes[-1], len(commit_index)) if hashes else len(commit_index)


def has_full_question(path):
    with open(path, encoding="utf-8") as f:
        head = f.read(300)
    return "another approach" not in head


for topic in TOPICS:
    problems = []
    for folder in os.listdir(topic):
        d = os.path.join(topic, folder)
        if not os.path.isdir(d):
            continue
        files = [os.path.join(d, f) for f in os.listdir(d) if f.endswith(".py")]
        if not files:
            continue
        ranked = sorted(files, key=lambda p: (not has_full_question(p), first_commit(p), p))
        problems.append((min(first_commit(p) for p in files), ranked))
    for _, files in sorted(problems):
        for p in files:
            print(p)

"""Print the .py files in commit order: all NeetCode problems first, then Codility.

Problems are ordered by the first commit that added any of their files. Inside a
problem folder, the file holding the full question comes first, then the other
approaches in commit order. Renamed files, committed or not, are traced back to
their original commit.
"""
import os
import subprocess

TOPICS = ["Data Structures & Algorithms", "codilty"]


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

"""Move NeetCode and Codility problem folders into their lesson folders.

NeetCode's GitHub sync always writes to `Data Structures & Algorithms/<problem>/`.
Run this after every pull: it moves any such folder (or new submission files for a
problem that is already organized) to

    Data Structures & Algorithms/<NN Section>/<N Lesson>/<problem>/

following NeetCode's "Algorithms and Data Structures for Beginners"
course. Problems outside the course go into extra sections after it.

Codility solutions are added by hand to `codility/<anything>/`; they move to
`codility/<NN Section>/<task-name>/`, using the same sections as NeetCode.

Files still named submission-N.py are listed at the end: they need a problem
statement and a proper name.

Usage: python3 scripts/organize.py [--dry-run]
"""
import os
import re
import subprocess
import sys

ROOT = "Data Structures & Algorithms"

# (section, lesson, [NeetCode problem ids]), in course order. Lesson folders are
# numbered by their position within the section here ("1 Static Arrays"), so the
# numbers never shift as more lessons get solved. Problem ids are the folder names the
# sync creates. The course lists more practice problems than you've solved; those
# ids are included so they're sorted automatically when you submit them.
COURSE = [
    ("01 Arrays", "Static Arrays", ["max-consecutive-ones", "remove-element",
                                       "replace-elements-with-greatest-element-on-right-side"]),
    ("01 Arrays", "Dynamic Arrays", ["dynamicArray", "concatenation-of-array"]),
    ("01 Arrays", "Stacks", ["baseball-game", "validate-parentheses", "minimum-stack"]),
    ("02 Linked Lists", "Singly Linked Lists", ["singlyLinkedList", "reverse-a-linked-list",
                                                   "merge-two-sorted-linked-lists"]),
    ("02 Linked Lists", "Doubly Linked Lists", ["design-linked-list", "design-browser-history"]),
    ("02 Linked Lists", "Queues", ["queue", "number-of-students-unable-to-eat-lunch",
                                      "implement-stack-using-queues"]),
    ("03 Recursion", "Factorial", ["factorial"]),
    ("03 Recursion", "Fibonacci Sequence", ["fibonacci", "climbing-stairs"]),
    ("04 Sorting", "Insertion Sort", ["insertionSort"]),
    ("04 Sorting", "Merge Sort", ["mergeSort", "merge-sorted-array", "merge-k-sorted-linked-lists"]),
    ("04 Sorting", "Quick Sort", ["quickSort"]),
    ("04 Sorting", "Bucket Sort", ["bucketSort", "sort-colors"]),
    ("05 Binary Search", "Search Array", ["binary-search", "search-2d-matrix"]),
    ("05 Binary Search", "Search Range", ["guess-number-higher-or-lower", "eating-bananas"]),
    ("06 Trees", "Binary Search Tree", ["search-in-a-binary-search-tree",
                                           "lowest-common-ancestor-in-binary-search-tree"]),
    ("06 Trees", "BST Insert and Remove", ["insert-into-a-binary-search-tree", "delete-node-in-a-bst"]),
    ("06 Trees", "Depth-First Search", ["binary-tree-inorder-traversal", "balanced-binary-tree",
                                           "kth-smallest-integer-in-bst",
                                           "binary-tree-from-preorder-and-inorder-traversal"]),
    ("06 Trees", "Breadth-First Search", ["level-order-traversal-of-binary-tree",
                                             "binary-tree-right-side-view"]),
    ("07 Backtracking", "Tree Maze", ["path-sum", "subsets", "combination-target-sum"]),
    ("08 Heap - Priority Queue", "Push and Pop", ["kth-largest-integer-in-a-stream"]),
    ("08 Heap - Priority Queue", "Heapify", ["last-stone-weight", "k-closest-points-to-origin",
                                                "kth-largest-element-in-an-array"]),
    ("09 Hashing", "Hash Usage", ["duplicate-integer", "two-integer-sum", "is-anagram", "lru-cache"]),
    ("10 Graphs", "Matrix DFS", ["matrixDFS", "flood-fill", "count-number-of-islands",
                                    "max-area-of-island"]),
    ("10 Graphs", "Matrix BFS", ["matrixBFS", "shortest-path-in-binary-matrix", "rotting-fruit"]),
    ("10 Graphs", "Adjacency List", ["clone-graph", "course-schedule"]),
    ("11 Dynamic Programming", "1-Dimension DP", ["house-robber"]),
    ("11 Dynamic Programming", "2-Dimension DP", ["count-paths", "count-unique-paths-ii",
                                                     "longest-common-subsequence"]),
    ("12 Bit Manipulation", "Bit Operations", ["number-of-one-bits", "counting-bits", "reverse-bits"]),
    # Not part of the beginners course (NeetCode 150 topics).
    ("13 Sliding Window", "", ["buy-and-sell-crypto", "longest-substring-without-duplicates"]),
    ("16 Greedy", "", ["maximum-subarray"]),       # same numbers as the codility/ sections
]

def lesson_dirs():
    """(section, lesson) -> numbered lesson folder, e.g. "01 Arrays/1 Static Arrays"."""
    dirs, count = {}, {}
    for section, lesson, _ in COURSE:
        if lesson:
            count[section] = count.get(section, 0) + 1
            dirs[section, lesson] = os.path.join(ROOT, section, f"{count[section]} {lesson}")
        else:
            dirs[section, lesson] = os.path.join(ROOT, section)
    return dirs


LESSON_DIR = lesson_dirs()
LOCATION = {pid: LESSON_DIR[section, lesson] for section, lesson, pids in COURSE for pid in pids}
SECTION_DIR = re.compile(r"^\d\d ")

# Codility: same sections (names and numbers) as the NeetCode tree, chosen by the
# technique each task uses. Sections the beginners course doesn't have use the
# NeetCode 150 topic names, numbered after 13 Sliding Window. No lesson level:
# codility/<NN Section>/<task-name>/. Includes the other Codility lesson tasks so
# new ones are sorted automatically.
CODILITY_ROOT = "codility"
CODILITY = [
    ("01 Arrays", ["cyclic-rotation", "max-counters",
                   "brackets", "fish", "nesting", "stone-wall"]),          # incl. stacks
    ("02 Linked Lists", ["arr-list-len"]),
    ("04 Sorting", ["distinct", "max-product-of-three", "triangle", "number-of-disc-intersections"]),
    ("05 Binary Search", ["min-max-division", "nailing-planks"]),
    ("09 Hashing", ["perm-missing-elem", "frog-river-one", "missing-integer", "perm-check",
                    "odd-occurrences-in-array", "dominator", "equi-leader"]),
    ("11 Dynamic Programming", ["number-solitaire", "min-abs-sum", "fib-frog", "ladder",
                                "max-slice-sum", "max-double-slice-sum"]),
    ("12 Bit Manipulation", ["binary-gap"]),
    ("13 Sliding Window", ["count-distinct-slices", "count-bounded-slices", "max-profit"]),
    ("14 Prefix Sums", ["tape-equilibrium", "passing-cars", "genomic-range-query",
                        "min-avg-two-slice"]),
    ("15 Two Pointers", ["abs-distinct", "count-triangles", "min-abs-sum-of-two"]),
    ("16 Greedy", ["max-nonoverlapping-segments", "tie-ropes"]),
    ("17 Math & Geometry", ["frog-jmp", "count-div", "count-factors", "min-perimeter-rectangle",
                            "flags", "peaks", "count-non-divisible", "count-semiprimes",
                            "chocolates-by-numbers", "common-prime-divisors"]),
]
CODILITY_LOCATION = {task: os.path.join(CODILITY_ROOT, lesson)
                     for lesson, tasks in CODILITY for task in tasks}
# Folder names used before that don't match the task name.
CODILITY_ALIASES = {"prem-missing-element": "perm-missing-elem",
                    "distinct-slices": "count-distinct-slices"}


def codility_task(folder):
    """'8 distinct slices' -> 'count-distinct-slices'."""
    name = re.sub(r"^\d+\s+", "", folder).strip().lower()
    name = re.sub(r"[\s_]+", "-", name)
    return CODILITY_ALIASES.get(name, name)


def git(*args):
    subprocess.run(["git", *args], check=True)


def move(src, dst, dry):
    print(f"  {src}  ->  {dst}")
    if dry:
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    os.rename(src, dst)
    git("add", "-A", "--", src, dst)


def organize(root, location, task_name=lambda name: name, is_lesson=SECTION_DIR.match):
    """Move every loose problem folder in root into its lesson. Returns unknown names."""
    unknown = []
    if not os.path.isdir(root):
        return unknown
    dry = "--dry-run" in sys.argv
    for name in sorted(os.listdir(root)):
        src = os.path.join(root, name)
        if not os.path.isdir(src) or is_lesson(name):
            continue
        task = task_name(name)
        if task not in location:
            unknown.append(src)
            continue
        dst = os.path.join(location[task], task)
        if not os.path.exists(dst):
            move(src, dst, dry)
            continue
        # Problem already organized: this is a new submission for it.
        for f in sorted(os.listdir(src)):
            move(os.path.join(src, f), os.path.join(dst, f), dry)
        if not dry:
            os.rmdir(src)
    return unknown


def main():
    unknown = organize(ROOT, LOCATION)
    codility_lessons = {lesson for lesson, _ in CODILITY}
    unknown += organize(CODILITY_ROOT, CODILITY_LOCATION, codility_task,
                        is_lesson=lambda name: name in codility_lessons)

    if unknown:
        print("\nNot in the map (add them to COURSE or CODILITY in organize.py):")
        for path in unknown:
            print("  " + path)

    todo = sorted(os.path.join(d, f) for d, _, files in os.walk(ROOT)
                  for f in files if re.fullmatch(r"submission-\d+\.py", f))
    if todo:
        print("\nStill need a problem statement and a proper name:")
        for p in todo:
            print("  " + p)


if __name__ == "__main__":
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # repo root
    main()

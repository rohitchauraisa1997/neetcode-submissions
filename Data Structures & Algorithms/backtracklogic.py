"""
BACKTRACKING: GENERIC LOGIC

Core idea: CHOOSE → EXPLORE → UN-CHOOSE
  Build a candidate step by step. If a branch can't lead to a goal, undo the
  last choice and try the next option.

Three problem types:
  | Type                | Explore step                       | Example                   |
  |---------------------|------------------------------------|---------------------------|
  | Find ONE            | if recurse(): return True          | canReachLeaf, hasPathSum  |
  | Find ALL            | recurse() and collect path[:]      | Path Sum II, subsets      |
  | Count / optimise    | total += recurse() / min(...)      | number of paths           |

When do you need pop() (un-choose)?
  - SHARED MUTABLE state (list, set, visited grid) → YES, undo the change.
  - IMMUTABLE value passed as an argument (int sum, string) → NO.
    It can't be changed in place: `sum -= x` makes a NEW local value and the
    caller's value stays as it was, so there's nothing to undo.
  - A NEW list passed down each call, e.g. dfs(child, path + [node.val]) → NO.
    Each call gets its own list, so nothing is shared. Simpler, but it costs
    an O(h) copy per call.

⚠️ Common mistakes:
  1. `return recurse(left)` alone skips the right side. Use `if recurse(left): return True`,
     or `return recurse(left) or recurse(right)` (`or` only tries right if left fails).
  2. res.append(path) stores a REFERENCE, which is empty after all the pops.
     Use path[:] or list(path).
  3. Forgetting pop() on shared state leaks the path between sibling branches.
  4. Double-counting: if you already did `remaining -= node.val`, don't subtract it again in the call.
  5. Leaf check: decide whether you compare BEFORE or AFTER using the current node, and stay consistent.
"""


# ---------------------------------------------------------------------------
# GENERIC TEMPLATE (pseudocode: invalid, is_goal, options, next_state,
# record, current and path are placeholders, so this doesn't run as-is)
# ---------------------------------------------------------------------------
def backtrack(state):
    # 1. DEAD END: invalid or out of bounds
    if invalid(state):
        return False

    # 2. CHOOSE: add the current element to the shared path
    path.append(current)

    # 3. GOAL CHECK
    if is_goal(state):
        record(path[:])       # or `return True` for find-one problems

    # 4. EXPLORE: try every option
    for option in options(state):
        if backtrack(next_state(option)):
            return True       # find-one only; drop this line for find-all

    # 5. UN-CHOOSE: undo step 2 so siblings start clean
    path.pop()
    return False


# ---------------------------------------------------------------------------
# NeetCode: Backtracking (Trees)
# Problem: Is there a root-to-leaf path that contains NO zeros?
#
#          4
#         / \
#        0   1          canReachLeaf → True  (4 → 1 → 2)
#             \         leafPath     → path = [4, 1, 2]
#              2
#
# canReachLeaf answers YES/NO. leafPath also returns WHICH path.
# ---------------------------------------------------------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 0. FIND ONE, no state at all → no pop()
#    Achieves: True if any root-to-leaf path avoids every 0-valued node.
#    A 0 node acts as a wall: that branch is a dead end.
def canReachLeaf(root):
    if not root or root.val == 0:              # 1. dead end: no node, or a blocked node
        return False

    if not root.left and not root.right:       # 3. goal: a leaf reached without hitting a 0
        return True
    if canReachLeaf(root.left):                # 4. explore left, stop on success
        return True
    if canReachLeaf(root.right):               #    left failed → try right
        return True
    return False                               # both sides blocked
    # No choose/un-choose steps: nothing is tracked, so there's nothing to undo.


# 1. FIND ONE + shared state → needs pop()
#    Achieves: same check as canReachLeaf, but `path` ends up holding the
#    actual valid path (e.g. [4, 1, 2]). If no path exists, `path` is left empty.
def leafPath(root, path):
    if not root or root.val == 0:              # 1. dead end
        return False
    path.append(root.val)                      # 2. choose: tentatively add this node

    if not root.left and not root.right:       # 3. goal: reached a leaf
        return True                            #    ⚠️ no pop: keep the path, it's the answer
    if leafPath(root.left, path):              # 4. explore left
        return True
    if leafPath(root.right, path):             #    explore right
        return True

    path.pop()                                 # 5. un-choose: this node led nowhere,
    return False                               #    remove it before the parent tries its other child


# ---------------------------------------------------------------------------
# 2. FIND ONE + immutable state → no pop()
#    LeetCode 112: does any root-to-leaf path sum to targetSum?
# ---------------------------------------------------------------------------
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:                                    # 1. dead end
            return False

        targetSum -= root.val                           # 2. choose (local int copy)

        if not root.left and not root.right:            # 3. goal
            return targetSum == 0                       # ⚠️ compared AFTER subtracting

        if self.hasPathSum(root.left, targetSum):       # 4. explore
            return True                                 # ⚠️ don't `return` the left result directly
        if self.hasPathSum(root.right, targetSum):
            return True

        return False                                    # 5. nothing to undo: int is passed by value


# ---------------------------------------------------------------------------
# 3. FIND ALL + shared state → needs pop() AND copy on record
#    LeetCode 113: return every root-to-leaf path that sums to targetSum.
# ---------------------------------------------------------------------------
def pathSum(root, targetSum):
    res, path = [], []

    def dfs(node, remaining):
        if not node:                                    # 1. dead end
            return
        path.append(node.val)                           # 2. choose
        remaining -= node.val

        if not node.left and not node.right and remaining == 0:
            res.append(path[:])                         # 3. goal ⚠️ COPY, `path` keeps changing

        dfs(node.left, remaining)                       # 4. explore both, no early exit
        dfs(node.right, remaining)

        path.pop()                                      # 5. un-choose

    dfs(root, targetSum)
    return res


# Time: O(n) for find-one/count on a tree.
#       O(n * h) for find-all on a tree (copying each path costs O(h)).
# Space: O(h) recursion + O(h) path
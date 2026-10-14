"""
Path Sum (NeetCode)
===================

You are given the root of a binary tree and an integer targetSum, return true
if the tree has a root-to-leaf path such that adding up all the values along
the path equals targetSum.

A leaf is a node with no children.

Example 1:
    Input:  root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: true
    Explanation: The root-to-leaf path 5 -> 4 -> 11 -> 2 sums to 22.

Example 2:
    Input:  root = [1,2,3], targetSum = 5
    Output: false
    Explanation: The root-to-leaf paths are 1 -> 2 (sum 3) and 1 -> 3 (sum 4).

Example 3:
    Input:  root = [], targetSum = 0
    Output: false
    Explanation: An empty tree has no root-to-leaf paths.

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:                # ⚠️ empty tree -> False, even if targetSum == 0
            return False

        # int is local to this call -> nothing to undo (no pop)
        # ⚠️ subtract only here, not again in the recursive calls
        targetSum = targetSum - root.val

        # ⚠️ goal only at a LEAF; [1,2], target 1 -> False (1 isn't a leaf)
        if not root.left and not root.right and targetSum==0:
            return True

        # ⚠️ not `return self.hasPathSum(root.left, ...)`: a False would skip the right side
        if self.hasPathSum(root.left, targetSum):
            return True
        if self.hasPathSum(root.right, targetSum):
            return True

        return False

# ⚠️ values can be negative: don't stop early when targetSum < 0
# Time: O(n), Space: O(h)
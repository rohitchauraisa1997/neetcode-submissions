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
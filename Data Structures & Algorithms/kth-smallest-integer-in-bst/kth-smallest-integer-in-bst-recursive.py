"""
Kth Smallest Integer in BST (NeetCode) -- another approach
Problem statement: see kth-smallest-integer-in-bst-iterative.py
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # RECURSIVE SOLN
        res = []

        def inorder(node):
            if node is None:
                return 

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)

        return res[k-1]

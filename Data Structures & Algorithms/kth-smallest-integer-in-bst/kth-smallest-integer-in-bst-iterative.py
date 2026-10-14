"""
Kth Smallest Integer in BST (NeetCode)
======================================

Given the root of a binary search tree, and an integer k, return the kth
smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:
    - The left subtree of every node contains only nodes with keys less than
      the node's key.
    - The right subtree of every node contains only nodes with keys greater
      than the node's key.
    - Both the left and right subtrees are also binary search trees.

Example 1:
    Input:  root = [2,1,3], k = 1
    Output: 1

Example 2:
    Input:  root = [4,3,5,2,null], k = 4
    Output: 5

Constraints:
    1 <= k <= The number of nodes in the tree <= 1000.
    0 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # ITERATIVE SOLN
        # Inorder traversal of a BST visits values in sorted order,
        # so the k-th node popped is the k-th smallest.
        stack = []
        curr = root
        n = 1  # 1-based count of popped nodes

        # ⚠️ Use `or`, not `and`. The stack is empty at the start, so `and` never enters the loop.
        while curr or stack:
            # Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            # ⚠️ Count on POP (that's the visit order). k is 1-based, so n starts at 1.
            if n == k:
                return curr.val  # Early exit, no need to traverse the rest
            n += 1

            curr = curr.right

# Time: O(h + k). We go down h levels, then pop k nodes, instead of O(n) for a full traversal.
# Space: O(h) for the stack
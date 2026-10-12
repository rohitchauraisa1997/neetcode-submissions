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
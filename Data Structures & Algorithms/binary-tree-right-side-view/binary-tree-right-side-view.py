"""
Binary Tree Right Side View (NeetCode)
======================================

You are given the root of a binary tree. Return only the values of the nodes
that are visible from the right side of the tree, ordered from top to bottom.

Example 1:
    Input:  root = [1,2,3]
    Output: [1,3]

Example 2:
    Input:  root = [1,2,3,4,5,6,7]
    Output: [1,3,7]

Constraints:
    0 <= number of nodes in the tree <= 100
    -100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS

        queue = deque()
        ans = []
        queue.append(root)

        while len(queue)>0:
            qlen = len(queue)
            rightSide = None
            for _ in range(qlen):
                popped = queue.popleft()
                if popped:
                    rightSide = popped
                    if popped.left:
                        queue.append(popped.left)
                    if popped.right:
                        queue.append(popped.right)

            # when the for loop finishes over the qlen rightSide will have the rightmost value unless None
            if rightSide:
                ans.append(rightSide.val)

        return ans
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS level by level: the queue holds every node of the current level,
        # we process them, and their children make up the next level.

        # ⚠️ Handle an empty tree up front, or you'd append None to the queue
        #    and crash on popped.val.
        if not root:
            return []

        # ⚠️ Use deque, not a list. list.pop(0) is O(n), deque.popleft() is O(1).
        queue = deque()
        queue.append(root)
        # level = 0
        ans = []

        while len(queue)>0:
            # ⚠️ KEY: snapshot the level size BEFORE the loop. Children get appended
            #    during the loop, so len(queue) keeps growing. Using it directly
            #    would mix the next level into this one.
            qlen = len(queue)
            # print(f"elements in level {level}")
            # level += 1
            levelArray = []
            for i in range(qlen):
                popped = queue.popleft()
                levelArray.append(popped.val)
                # Queue the children for the NEXT level, left before right so the order is preserved
                # ⚠️ Check for None before appending, or you'll pop None later.
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)

            # Exactly one level is done
            ans.append(levelArray)

        return ans

# Example:     3
#             / \
#            9   20      → [[3], [9, 20], [15, 7]]
#               /  \
#              15   7
#
# Time: O(n), every node is enqueued and dequeued once
# Space: O(w), where w = max width. That's up to ~n/2 for the last level of a full tree.
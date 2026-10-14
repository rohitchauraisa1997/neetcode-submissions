"""
Delete Node in a BST (NeetCode)
===============================

You are given a root node reference of a BST and a key, delete the node with
the given key in the BST, if present. Return the root node reference (possibly
updated) of the BST after deletion.

Basically, the deletion can be divided into two stages:
    1. Search for a node to remove.
    2. If the node is found, delete the node.

Note: There can be multiple results after deleting the node, return any one of
them.

Example 1:
    Input:  root = [5,3,9,1,4], key = 3
    Output: [5,4,9,1]
    Explanation: Another valid answer is [5,1,9,null,4].

Example 2:
    Input:  root = [5,3,6,2,4,null,7], key = 0
    Output: [5,3,6,2,4,null,7]
    Explanation: The tree does not contain a node with value 0.

Constraints:
    The number of nodes in the tree is in the range [0, 10^4].
    -10^5 <= key, Node.val <= 10^5
    All the values Node.val are unique.
    root is a valid binary search tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMinValue(self, root):
        # Smallest value in a BST = leftmost node
        # ⚠️ Go LEFT only. Not right, and not a full traversal.
        while root and root.left:
            root = root.left
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Returns the new root of this subtree; the parent reattaches it.
        if not root:
            return None  # ⚠️ Key not in the tree. Don't forget this base case.

        # Search: go left/right using the BST property
        # ⚠️ Assign the result back. Deletion can change the child's root.
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # Found it.
            # 0 or 1 child: replace the node with its only child (or None)
            # ⚠️ A leaf is handled here too: root.right is None, so it returns root.left (also None).
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            # 2 children: copy the inorder successor (min of the right subtree)
            # into this node, then delete that successor from the right subtree
            # ⚠️ Search for the min in root.RIGHT, not in root.
            # ⚠️ Recurse on root.right with min_val, NOT with key.
            #    key is already overwritten and doesn't exist down there.
            else:
                min_val = self.findMinValue(root.right)
                root.val = min_val
                root.right = self.deleteNode(root.right, min_val)

        return root

# Time/space: O(h), where h = log n if balanced, n if skewed
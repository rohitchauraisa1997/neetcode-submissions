"""
Insert into a Binary Search Tree (NeetCode)
===========================================

You are given the root node of a binary search tree (BST) and a value val to
insert into the tree. Return the root node of the BST after the insertion. It is
guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the
tree remains a BST after insertion. You can return any of them.

Example 1:
    Input:  root = [4,2,7,1,3], val = 5
    Output: [4,2,7,1,3,5]

Example 2:
    Input:  root = [40,20,60,10,30,50,70], val = 25
    Output: [40,20,60,10,30,50,70,null,null,25]

Constraints:
    The number of nodes in the tree is in the range [0, 10^4].
    -10^8 <= Node.val <= 10^8
    All the values Node.val are unique.
    -10^8 <= val <= 10^8
    It's guaranteed that val does not exist in the original BST.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Returns the new root of this subtree; the parent reattaches it.

        # Empty spot found: the new node goes here
        # ⚠️ Must RETURN the new node. Creating it without returning means it never gets attached.
        # ⚠️ Also covers an empty tree: the caller gets the new node back as the root.
        if root is None:
            return TreeNode(val)

        # Walk down using the BST property
        # ⚠️ Assign the result back (root.left = ...). Just calling
        #    self.insertIntoBST(root.left, val) loses the new node when root.left is None.
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        # val == root.val: duplicate, so do nothing
        # ⚠️ Check the problem's rule on duplicates; some want them sent left or right.

        # ⚠️ Return the original root, not the new node.
        return root

# Time/space: O(h), where h = log n if balanced, n if skewed
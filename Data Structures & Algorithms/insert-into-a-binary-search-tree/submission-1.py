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
"""
Construct Binary Tree from Preorder and Inorder Traversal (NeetCode)
====================================================================

You are given two integer arrays preorder and inorder.
    - preorder is the preorder traversal of a binary tree
    - inorder is the inorder traversal of the same tree
    - Both arrays are of the same size and consist of unique values.

Rebuild the binary tree from the preorder and inorder traversals and return its
root.

Example 1:
    Input:  preorder = [1,2,3,4], inorder = [2,1,3,4]
    Output: [1,2,3,null,null,null,4]

Example 2:
    Input:  preorder = [1], inorder = [1]
    Output: [1]

Constraints:
    1 <= inorder.length <= 1000.
    inorder.length == preorder.length
    -1000 <= preorder[i], inorder[i] <= 1000
    preorder and inorder consist of unique values.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder helps us find the main root node 
        # and then inorder helps us find the left and 
        # right BT by indexing the value of the root node value
        # ┌─────────────────────────────────────────────────────────────┐
        # │ VISUAL (Example 1)                                          │
        # │                                                             │
        # │            3            preorder = [3, 9, 20, 15, 7]        │
        # │          /   \          inorder  = [9, 3, 15, 20, 7]        │
        # │         9     20                                            │
        # │              /  \                                           │
        # │            15    7                                          │
        # │                                                             │
        # │ 1) PREORDER (Root, Left, Right): the first element is ROOT  │
        # │      [ 3 | 9 | 20, 15, 7 ]                                  │
        # │        ↑   └┬┘ └───┬───┘                                    │
        # │      root  left   right                                     │
        # │            (1)     (3)     ← sizes come from the inorder!   │
        # │                                                             │
        # │ 2) INORDER (Left, Root, Right): find the root, split there  │
        # │      [ 9 | 3 | 15, 20, 7 ]                                  │
        # │        └┬┘  ↑  └───┬────┘                                   │
        # │       left mid   right                                      │
        # │       (1)        (3)                                        │
        # │                                                             │
        # │ Preorder tells us WHO the root is.                          │
        # │ Inorder tells us HOW MANY nodes go left/right (mid = 1).    │
        # │ That count lets us cut preorder too: the root, then the     │
        # │ next `mid` items are the left subtree, the rest are right.  │
        # │ Recurse on each side with the matching pieces of both lists.│
        # └─────────────────────────────────────────────────────────────┘

        # ⚠️ Use `not`, not `is None`. Slicing produces [], never None,
        #    so `is None` never fires and preorder[0] then raises IndexError.
        if not preorder or not inorder:
            return None
 
        # Step 1: preorder gives the root
        root = TreeNode(preorder[0])

        # Step 2: find the root in inorder. mid = index = SIZE of the left subtree.
        # ⚠️ Works only because values are unique.
        mid = inorder.index(preorder[0])

        # Step 3: cut both lists with the same sizes and recurse
        #   preorder: [root | left (mid items) | right ]
        #              0      1 .. mid           mid+1 ..
        #   inorder:  [left (mid items) | root | right ]
        #              0 .. mid-1         mid    mid+1 ..
        # ⚠️ The root is excluded from both sides: preorder starts at 1, and inorder skips mid.
        # ⚠️ preorder[1:mid+1], not [1:mid]. The slice end is exclusive, and we need `mid` items.
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

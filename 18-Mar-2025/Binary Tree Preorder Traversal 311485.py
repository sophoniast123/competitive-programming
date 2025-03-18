# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def travesal_preorder(root,arr):
            if root is not None:
                arr.append(root.val)
                travesal_preorder(root.left,arr)
                travesal_preorder(root.right,arr)

        travesal_preorder(root,arr)
        return arr
        

        
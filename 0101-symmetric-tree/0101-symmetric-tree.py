# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(leftTree, rightTree):
            if not leftTree and not rightTree:
                return True
            if not leftTree or not rightTree:
                return False
            if leftTree.val != rightTree.val:
                return False
            return helper(leftTree.left, rightTree.right) and helper(leftTree.right, rightTree.left)

        return helper(root.left, root.right)
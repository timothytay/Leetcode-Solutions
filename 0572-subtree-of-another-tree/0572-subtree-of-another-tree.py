# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif (root1 and not root2) or (root2 and not root1):
            return False
        elif root1.val != root2.val:
            return False
        else:
            return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
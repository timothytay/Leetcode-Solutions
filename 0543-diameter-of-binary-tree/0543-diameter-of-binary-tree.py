# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        seen = {}
        def getDepth(root):
            if not root:
                return 0
            if root in seen:
                return seen[root]
            else:
                seen[root] = 1 + max(getDepth(root.left), getDepth(root.right))
                return seen [root]

        def getDiameter(root):
            if not root:
                return 0
            diameter = getDepth(root.right) + 1 + getDepth(root.left)
            return max(diameter, getDiameter(root.right), getDiameter(root.left))

        return getDiameter(root) - 1
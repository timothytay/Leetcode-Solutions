# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def getDepth(root):
            if not root or not self.balanced:
                return 0
            left = getDepth(root.left)
            right = getDepth(root.right)
            if abs(left - right) > 1:
                self.balanced = False
            return 1 + max(left, right)
        getDepth(root)
        return self.balanced
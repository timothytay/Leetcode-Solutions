# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root, max, min):
            return not root or (root.val < max and root.val > min and valid(root.left, root.val, min) and valid(root.right, max, root.val))

        return valid(root, float('inf'), float('-inf'))
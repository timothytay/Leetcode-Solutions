# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def getMaxSum(root):
            if not root:
                return 0
            nonlocal maxSum
            leftMax = getMaxSum(root.left)
            rightMax = getMaxSum(root.right)
            maxSum = max(maxSum, (leftMax if leftMax > 0 else 0) + (rightMax if rightMax > 0 else 0) + root.val)
            return root.val + max(leftMax, rightMax, 0)
        getMaxSum(root)
        return maxSum
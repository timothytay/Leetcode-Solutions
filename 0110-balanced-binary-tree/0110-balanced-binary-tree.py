# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # if leaf node or node is null, return 0
        # get the max depth or left and right subtrees
        # if difference is more than 1
        # return false
        # otherwise continue for left and right nodes and their subtrees

        # might be interesting to see whether to return a bool or the value of the depth

        
        answer = True
        def dfs(root):
            nonlocal answer
            if not root:
                return 0
            leftDepth = dfs(root.left)
            rightDepth = dfs(root.right)
            if abs(rightDepth - leftDepth) > 1:
                answer = False
            return 1 + max(leftDepth, rightDepth)
        dfs(root)
        return answer
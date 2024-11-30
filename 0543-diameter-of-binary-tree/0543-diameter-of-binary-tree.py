# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # for each node, check largest length with traversal
        # get maximum depth of left subtree and max of right subtree
        # start at 0 when reaching leaf node, add 1 per future node to get edges
        diameter = 0
        
        def longestPath(root):
            if not root:
                return 0
            nonlocal diameter
            leftLongest = longestPath(root.left)
            rightLongest = longestPath(root.right)
            diameter = max(diameter, leftLongest + rightLongest)
            return 1 + max(leftLongest, rightLongest)

        longestPath(root)
        return diameter
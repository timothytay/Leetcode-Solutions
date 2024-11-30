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
        cache = {}
        def getMaxDepth(node):
            if not node or (not node.left and not node.right):
                return 0
            else:
                if node in cache:
                    return cache[node]
                else:
                    cache[node] = 1 + max(getMaxDepth(node.left), getMaxDepth(node.right))
                    return cache[node]
        def dfs(node):
            if node and node.left and node.right:
                maxDiameter = getMaxDepth(node.left) + getMaxDepth(node.right) + 2
            elif node and node.left:
                maxDiameter = getMaxDepth(node.left) + 1
            elif node and node.right:
                maxDiameter = getMaxDepth(node.right) + 1
            else:
                return 0

            return max(maxDiameter, dfs(node.left), dfs(node.right))
            
        return dfs(root)
        
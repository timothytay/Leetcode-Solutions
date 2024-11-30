# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # DFS
        # if the current node is null return 0
        # else, if the current node is larger or equal that the maximum so far
        # return 1 + the recursive function, updating the current largest if necessary

        def dfs(root, curLargest):
            if not root:
                return 0
            if root.val >= curLargest:
                largest = max(curLargest, root.val)
                return 1 + dfs(root.left, largest) + dfs(root.right, largest)
            else:
                return dfs(root.left, curLargest) + dfs(root.right, curLargest)
        return dfs(root, root.val)


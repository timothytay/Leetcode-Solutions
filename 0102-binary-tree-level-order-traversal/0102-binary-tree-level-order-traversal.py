# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque()
        q.appendleft(root)
        while len(q) > 0:
            level = []
            for i in range(len(q)):
                node = q.pop()
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
                level.append(node.val)
            ans.append(level)
        return ans
from collections import deque

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
        res = []
        q = deque()
        q.appendleft(root)
        while len(q) > 0:
            curRes = []
            for i in range(len(q)):
                curNode = q.pop()
                curRes.append(curNode.val)
                if curNode.left:
                    q.appendleft(curNode.left)
                if curNode.right:
                    q.appendleft(curNode.right)
            res.append(curRes)
        return res
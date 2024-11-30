# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        dq = deque()
        dq.appendleft(root)
        while len(dq) > 0:
            res.append(dq[-1].val)
            for i in range(len(dq)):
                cur = dq.pop()
                if cur.right:
                    dq.appendleft(cur.right)
                if cur.left:
                    dq.appendleft(cur.left)

        return res
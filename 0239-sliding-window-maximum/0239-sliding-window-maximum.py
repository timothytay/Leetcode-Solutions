from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(k):
            if not q:
                q.append(i)
            else:
                while q and nums[i] > nums[q[-1]]:
                    q.pop()
                q.append(i)
        res.append(nums[q[0]])
        l = 0
        for r in range(k, len(nums)):
            if l == q[0]:
                q.popleft()
            l += 1
            while q and nums[r] >= nums[q[-1]]:
                q.pop()          
            q.append(r)
            res.append(nums[q[0]])
        return res
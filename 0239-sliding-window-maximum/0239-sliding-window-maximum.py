class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = deque()
        for i in range(len(nums)):
            while dq and dq[0][1] <= i - k:
                dq.popleft()
            if not dq or dq[-1][0] > nums[i]:
                dq.append((nums[i], i))
            else:
                while dq and nums[i] >= dq[-1][0]:
                    dq.pop() 
                dq.append((nums[i], i))
            if i >= k - 1:
                
                ans.append(dq[0][0])
        return ans
                


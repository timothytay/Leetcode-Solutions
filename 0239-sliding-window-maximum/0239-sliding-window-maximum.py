class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = deque()
        for i in range(len(nums)):
            while dq and dq[0] <= i - k:
                dq.popleft()
            if not dq or nums[dq[-1]] > nums[i]:
                dq.append(i)
            else:
                while dq and nums[i] >= nums[dq[-1]]:
                    dq.pop() 
                dq.append(i)
            if i >= k - 1:    
                ans.append(nums[dq[0]])
        return ans
                
    # remove ones that fall out of window on left
    # add to right when current is smaller because it might be used later
    # if current is bigger than rightmost, remove right until it is smaller then add
    # this is because if it is bigger and more recent, the previous rightmost will never be used


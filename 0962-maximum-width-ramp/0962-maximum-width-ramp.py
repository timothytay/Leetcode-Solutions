class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxWidth = 0
        stack = []
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                maxWidth = max(maxWidth, i - stack[-1])
                stack.pop()
        return maxWidth
            
            

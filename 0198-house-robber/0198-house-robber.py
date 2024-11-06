class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        if len(nums) < 2:
            return nums[0]
        
        for i in range(len(nums)-3, -1, -1):
            nums[i] = nums[i] + max(nums[i+2], (nums[i+3] if i + 3 < len(nums) else 0))

        return max(nums[0], nums[1])

        

        
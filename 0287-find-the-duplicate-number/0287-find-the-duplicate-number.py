class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            else:
                nums[nums[i]] *= -1
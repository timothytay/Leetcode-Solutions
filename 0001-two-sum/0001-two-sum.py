class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {} # number : index
        for i, num in enumerate(nums):
            if target - num in seen:
                return [i, seen[target - num]]
            else:
                seen[num] = i
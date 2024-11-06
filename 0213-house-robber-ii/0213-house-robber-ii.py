class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        if len(nums) == 1:
            return nums[0]
        def robHouse(house, zero):
            if house >= len(nums):
                return 0
            if zero and house == len(nums) - 1:
                return 0
            if (house, zero) in memo:
                return memo[(house, zero)]
            memo[(house, zero)] = nums[house] + max(robHouse(house+2, zero), robHouse(house+3, zero))
            return memo[(house, zero)]

        return max(robHouse(0, True), robHouse(1, False), robHouse(2, False))
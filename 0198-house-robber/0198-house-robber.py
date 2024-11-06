class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}

        def robHouse(house):
            if house >= len(nums):
                return 0
            if house in memo:
                return memo[house]
            memo[house] = nums[house] + max(robHouse(house+2), robHouse(house+3))
            return memo[house]
            
        return max(robHouse(0), robHouse(1))
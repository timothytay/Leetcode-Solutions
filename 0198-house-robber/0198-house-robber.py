class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        """
        def robHouse(house):
            if house >= len(nums):
                return 0
            if house in memo:
                return memo[house]
            memo[house] = nums[house] + max(robHouse(house+2), robHouse(house+3))
            return memo[house]

        return max(robHouse(0), robHouse(1))
        """

        if len(nums) < 2:
            return nums[0]
        dp = nums[:]
        for i in range(len(dp)-3, -1, -1):
            dp[i] = dp[i] + max(dp[i+2], (dp[i+3] if i + 3 < len(dp) else 0))

        return max(dp[0], dp[1])
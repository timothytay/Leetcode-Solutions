class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums[0], self.houseRob(nums[1:]), self.houseRob(nums[:-1]))

    def houseRob(self, nums):
        dp = nums
        for i in range(len(dp)-3, -1, -1):
            dp[i] = dp[i] + max(dp[i+2], dp[i+3] if i + 3 < len(dp) else 0)
        return max(dp[:2]) if dp else 0

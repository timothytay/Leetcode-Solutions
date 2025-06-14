class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(nums[i] + (dp[i+2] if i+2 < len(nums) else 0),
                        nums[i] + (dp[i+3] if i+3 < len(nums) else 0))
        return max(dp[0], (dp[1] if 1 < len(nums) else dp[0]))
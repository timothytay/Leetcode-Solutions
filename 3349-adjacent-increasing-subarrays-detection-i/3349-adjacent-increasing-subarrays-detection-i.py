class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        dp = [1] * len(nums)
        for i in range(len(dp) - 2, -1, -1):
            if nums[i+1] > nums[i]:
                dp[i] = 1 + dp[i+1]

        for i in range(len(dp)):
            if dp[i] >= 2 * k:
                return True
            if dp[i] >= k and i + k < len(dp) and dp[i+k] >= k:
                return True

        return False
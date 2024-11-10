class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(dp)-2, -1, -1):
            tempCurDP = dp[i]
            for j in range(i+1, len(dp)):
                
                if nums[j] > nums[i] and tempCurDP + dp[j] > dp[i]:
                    dp[i] = tempCurDP + dp[j]

        return max(dp) 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums)-2, -1, -1):
            if True in dp[i:i+nums[i]+1]:
                dp[i] = True
        return dp[0]
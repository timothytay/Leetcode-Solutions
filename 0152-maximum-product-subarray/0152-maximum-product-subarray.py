import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        maxDP = [0] * len(nums)
        minDP = [0] * len(nums)

        maxDP[0], minDP[0] = nums[0], nums[0]

        for i in range(1, len(nums)):
            
            maxDP[i] = max(nums[i] * maxDP[i-1], nums[i] * minDP[i-1], nums[i])
            minDP[i] = min(nums[i] * maxDP[i-1], nums[i] * minDP[i-1], nums[i])
            maxProd = max(maxDP[i], maxProd)

        return maxProd
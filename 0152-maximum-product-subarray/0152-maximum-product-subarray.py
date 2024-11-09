import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        maximum = nums[0]
        minimum = nums[0]

        for i in range(1, len(nums)):
            
            maximum = max(nums[i] * maximum, nums[i] * minimum, nums[i])
            minimum = min(nums[i] * maximum, nums[i] * minimum, nums[i])
            maxProd = max(maximum, maxProd)

        return maxProd
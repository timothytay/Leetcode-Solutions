class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mins, maxs = [0] * len(nums), [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if i+1 >= len(nums):
                mins[i] = maxs[i] = nums[i]
            else:
                maxs[i] = max(nums[i] * maxs[i+1], nums[i] * mins[i+1], nums[i])
                mins[i] = min(nums[i] * maxs[i+1], nums[i] * mins[i+1], nums[i])

        return max(maxs)

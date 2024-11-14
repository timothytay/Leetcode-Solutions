class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = nums[0]
        for i in range(len(nums)):
            if i <= furthest and i + nums[i] > furthest:
                furthest = i + nums[i]
        return furthest >= len(nums) - 1


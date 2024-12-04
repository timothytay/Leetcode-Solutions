class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = {}
        for i in range(len(nums)):
            freqs[nums[i]] = 1 + freqs.get(nums[i], 0)
            if freqs[nums[i]] > len(nums) // 2:
                return nums[i]

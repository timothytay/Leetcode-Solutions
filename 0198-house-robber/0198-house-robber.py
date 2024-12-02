class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def robHouse(i):
            nonlocal nums
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = nums[i] + max(robHouse(i+2), robHouse(i+3))
            return cache[i]
        return max(robHouse(0), robHouse(1))
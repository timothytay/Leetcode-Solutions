class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        target = numSum // 2
        if numSum % 2:
            return False
        #cache = {}
        @lru_cache(maxsize = None)
        def helper(target, i):
            nonlocal nums, numSum
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False

            #if (sum1, i) in cache:
            #    return cache[(sum1, i)]
            #cache[(sum1, i)] = helper(sum1 - nums[i], i + 1) or helper(sum1, i + 1)
            return helper(target - nums[i], i + 1) or helper(target, i + 1)
        

        return helper(target, 0)
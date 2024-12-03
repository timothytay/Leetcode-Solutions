class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        #cache = {}
        @lru_cache(maxsize = None)
        def helper(sum1, i):
            nonlocal nums, numSum
            if sum1 == numSum - sum1:
                return True
            if i >= len(nums):
                return False

            #if (sum1, i) in cache:
            #    return cache[(sum1, i)]
            #cache[(sum1, i)] = helper(sum1 - nums[i], i + 1) or helper(sum1, i + 1)
            return helper(sum1 - nums[i], i + 1) or helper(sum1, i + 1)
        return helper(sum(nums), 0)

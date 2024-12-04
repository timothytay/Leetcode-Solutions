class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSoFar = minSoFar = maxProduct = nums[0]

        for i in range(1, len(nums)):
            tmp_minSoFar = min(maxSoFar * nums[i], minSoFar * nums[i], nums[i])
            maxSoFar = max(maxSoFar * nums[i], minSoFar * nums[i], nums[i])
            minSoFar = tmp_minSoFar
            maxProduct = max(maxProduct, maxSoFar)

        return max(maxProduct, maxSoFar)

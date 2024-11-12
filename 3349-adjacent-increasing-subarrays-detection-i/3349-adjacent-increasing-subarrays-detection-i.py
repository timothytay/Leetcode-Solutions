class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            isIncreasing = True
            for j in range(1, k):
                if i + j >= len(nums) or i + j < len(nums) and nums[i+j] <= nums[i+j-1]:
                    isIncreasing = False
                    break

            for j in range(k+1, 2 * k):
                if i + j >= len(nums) or i + j < len(nums) and nums[i+j] <= nums[i+j-1]:
                    isIncreasing = False
                    break
            if isIncreasing:
                return True
        
        return False
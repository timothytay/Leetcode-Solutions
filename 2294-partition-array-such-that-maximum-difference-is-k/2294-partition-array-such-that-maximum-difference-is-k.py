class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        lowest = nums[0]
        count = 1

        for num in nums:
            if num - lowest > k:
                count += 1
                lowest = num
        return count
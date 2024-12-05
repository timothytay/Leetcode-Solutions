class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sums = {}
        sums[0] = 1
        curSum = 0
        count = 0
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum - k in sums:
                count += sums[curSum-k]
            sums[curSum] = 1 + sums.get(curSum, 0)
            
        
        return count
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        
        def works(k):
            diff = [0] * (len(nums) + 1)
            for l, r, v in queries[:k]:
                diff[l] += v
                diff[r+1] -= v
            for i in range(1, len(diff)):
                diff[i] = diff[i-1] + diff[i]
            for i in range(len(nums)):
                if diff[i] < nums[i]:
                    return False
            return True

        minWorks = float('inf')
        l, r = 0, len(queries)
        while l <= r:
            m = (l+r) // 2
            if not works(m):
                l = m + 1
            if works(m):
                minWorks = min(m, minWorks)
                r = m - 1
        return minWorks if minWorks < float('inf') else -1
            

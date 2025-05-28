class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            ans = min(ans, nums[mid])
            if nums[mid] < nums[-1]:
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
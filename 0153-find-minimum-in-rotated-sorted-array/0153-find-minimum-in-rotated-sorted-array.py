class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        curMin = nums[0]
        while l <= r:
            m = (l + r) // 2
            curMin = min(curMin, nums[m])
            if nums[r] >= nums[m]:
                r = m - 1
            else:
                l = m + 1
        return curMin
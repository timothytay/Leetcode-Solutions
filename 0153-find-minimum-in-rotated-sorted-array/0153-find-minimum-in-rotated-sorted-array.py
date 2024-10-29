class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minNum = float('inf')
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            minNum = min(minNum, nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return min(minNum, nums[0])
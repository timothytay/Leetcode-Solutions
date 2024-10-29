class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        mini = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] < mini:
                index = m
                mini = nums[m]
            elif nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
        def binarySearch(l, r, target):
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    return m
                if target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        left = binarySearch(0, index - 1, target)
        right = binarySearch(index, len(nums)-1, target)
        return left if left != -1 else right
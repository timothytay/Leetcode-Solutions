class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        m = (0 + len(nums)) // 2
        left = nums[:m]
        right = nums[m:]
        left = self.sortArray(left)
        right = self.sortArray(right)
        nums = self.merge(left, right)
        return nums


    def merge(self, l1, l2):
        res = []
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        if i < len(l1):
            res += l1[i:]
        if j < len(l2):
            res += l2[j:]
        return res
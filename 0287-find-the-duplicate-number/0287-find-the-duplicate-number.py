class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            cur = abs(nums[i])
            if nums[cur] < 0:
                return cur
            else:
                nums[cur] *= -1
            
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [0] * len(nums)
        suffix[-1] = 1
        for i in range(len(suffix) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        tmp = nums[0]
        nums[0] = 1
        for i in range(1, len(nums)):
            res = nums[i-1] * tmp 
            tmp = nums[i]
            nums[i] = res
        for i in range(len(suffix)):
            suffix[i] = suffix[i] * nums[i]
        return suffix
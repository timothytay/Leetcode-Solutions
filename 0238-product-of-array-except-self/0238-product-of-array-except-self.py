class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]

        for i in range(len(suffix)):
            suffix[i] = (suffix[i+1] if i + 1 < len(suffix) else 1) * (prefix[i-1] if i - 1 >= 0 else 1)
        
        return suffix
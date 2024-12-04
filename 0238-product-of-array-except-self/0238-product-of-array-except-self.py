class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # algorithm outline
        # compute prefix products
        # compute suffix products
        # multiply prefix and suffix products for each index
        # return 

        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        # 1, 1, 2, 6

        suffix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        # 24, 12, 4, 1

        for i in range(len(nums)):
            suffix[i] *= prefix[i]
        
        return suffix
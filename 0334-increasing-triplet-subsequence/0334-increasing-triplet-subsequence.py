class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        prefixMin = nums[:]
        for i in range(len(nums)):
            if i >= 1 and nums[i] < prefixMin[i-1]:
                prefixMin[i] = nums[i]
            else:
                prefixMin[i] = prefixMin[i-1 if i > 0 else i]
        postfixMax = nums[:]
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1 and nums[i] > postfixMax[i+1]:
                postfixMax[i] = nums[i]
            else:
                postfixMax[i] = postfixMax[i+1 if i+1 <= len(nums) - 1 else i]
        for i in range(len(nums)):
            if i > 0 and i < len(nums) - 1:
                if prefixMin[i-1] < nums[i] < postfixMax[i+1]:
                    return True
        return False

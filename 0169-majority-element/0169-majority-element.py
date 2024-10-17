class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freqs = {}
        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)
            if freqs[num] > len(nums) / 2:
                return num
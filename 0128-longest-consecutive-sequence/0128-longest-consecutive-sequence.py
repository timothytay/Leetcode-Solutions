class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        numSet = set(nums)
        for num in numSet:
            if num - 1 not in numSet:
                seq = 1
                cur = num
                while cur + 1 in numSet:
                    seq += 1
                    cur += 1
                longest = max(seq, longest)
        return longest
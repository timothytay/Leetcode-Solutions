from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in freqs.items():
            bucket[value].append(key)
        i = len(bucket) - 1
        res = []
        while k > 0:
            for num in bucket[i]:
                res.append(num)
                k -= 1
            i -= 1
        return res
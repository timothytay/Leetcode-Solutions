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

        topK = sorted(freqs.items(), key = lambda x:x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(topK[i][0])
        return res     
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqs = {}
        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)
        hp = []
        for num, freq in freqs.items():
            heapq.heappush(hp, (freq, num))
            if len(hp) > k:
                heapq.heappop(hp)
        res = []
        for freq, num in hp:
            res.append(num)
        return res
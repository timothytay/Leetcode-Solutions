class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        sortedFreqs = sorted(freqs.items(), key = lambda x : x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(sortedFreqs[i][0])
        return res

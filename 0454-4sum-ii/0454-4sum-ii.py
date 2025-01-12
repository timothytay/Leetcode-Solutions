class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        freqs = {}
        for num3 in nums3:
            for num4 in nums4:
                total = num3 + num4
                freqs[total] = 1 + freqs.get(total, 0)
        n = len(nums1)
        count = 0
        for i in range(n):
            for j in range(n):
                target = - nums1[i] - nums2[j]
                if target in freqs:
                    count += freqs[target]
        return count
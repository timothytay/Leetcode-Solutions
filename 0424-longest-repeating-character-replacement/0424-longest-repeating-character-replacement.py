class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLen = 0
        freqs = {}
        l = 0
        for r in range(0, len(s)):
            freqs[s[r]] = 1 + freqs.get(s[r], 0)
            while (r - l + 1 - max(freqs.values())) > k:
                freqs[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
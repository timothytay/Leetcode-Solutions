class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        freqs = {}
        l = 0
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            while r - l + 1 - max(freqs.values()) > k:
                freqs[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        maxLen = 0
        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[r])
            maxLen = max(maxLen, len(window))

        return maxLen
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        window = set()
        l = 0
        for r in range(0, len(s)):
            if s[r] not in window:
                window.add(s[r])
                maxLen = max(len(window), maxLen)
            else:
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
                window.add(s[r])
        return maxLen

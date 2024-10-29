from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tFreqs = defaultdict(int)
        for char in t:
            tFreqs[char] = tFreqs.get(char, 0) + 1
        window = defaultdict(int)
        l = 0
        have = 0
        need = len(tFreqs)
        substr = ""
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in tFreqs and window[s[r]] == tFreqs[s[r]]:
                have += 1
            while have == len(tFreqs):
                if r - l + 1 < len(substr) or substr == "":
                    substr = s[l:r+1]
                window[s[l]] -= 1
                if s[l] in tFreqs:
                    if window[s[l]] < tFreqs[s[l]]:
                        have -= 1
                l += 1
        return substr
        
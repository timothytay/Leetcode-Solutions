class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        ans = ""
        ansL, ansR = 0, float('inf')
        tFreqs = {}
        for char in t:
            tFreqs[char] = 1 + tFreqs.get(char, 0)
        sFreqs = {}
        have = 0
        need = len(tFreqs)
        l = 0
        for r in range(len(s)):
            sFreqs[s[r]] = 1 + sFreqs.get(s[r], 0)
            if s[r] in tFreqs and sFreqs[s[r]] == tFreqs[s[r]]:
                have += 1
            while have == need:
                if r - l < ansR - ansL:
                    ansR, ansL = r, l
                sFreqs[s[l]] -= 1
                if s[l] in tFreqs and tFreqs[s[l]] == sFreqs[s[l]] + 1:
                    have -= 1
                l += 1
        return s[ansL:ansR + 1] if ansR != float('inf') else ""


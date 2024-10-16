class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        freqs = {}
        for l in range(len(s)-minSize+1):
            slic = s[l:l+minSize]
            if len(set(slic)) <= maxLetters:
                freqs[slic] = 1 + freqs.get(slic, 0)
        return max(freqs.values()) if freqs.values() else 0

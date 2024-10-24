class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        maxFreq = 0
        freqs = {}
        for l in range(len(s) - minSize + 1):
            if len(set(s[l:l+minSize])) <= maxLetters:
                freqs[s[l:l+minSize]] = 1 + freqs.get(s[l:l+minSize], 0)
                maxFreq = max(freqs[s[l:l+minSize]], maxFreq)
        return maxFreq
                    

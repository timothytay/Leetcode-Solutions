from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Freqs = [0] * 26
        s2Freqs = [0] * 26
        for i in range(len(s1)):
            s1Freqs[ord(s1[i]) - ord('a')] += 1
            s2Freqs[ord(s2[i]) - ord('a')] += 1
        if s1Freqs == s2Freqs:
            return True
        for l in range(0, len(s2) - len(s1)):
            s2Freqs[ord(s2[l]) - ord('a')] -= 1
            s2Freqs[ord(s2[l + len(s1)]) - ord('a')] += 1
            if s1Freqs == s2Freqs:
                return True
        return False
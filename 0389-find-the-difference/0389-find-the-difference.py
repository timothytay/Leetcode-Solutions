class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCount, tCount = [0] * 26, [0] * 26
        for c in s:
            sCount[ord(c) - ord('a')] += 1
        for c in t:
            tCount[ord(c) - ord('a')] += 1
        for i in range(26):
            if sCount[i] + 1 == tCount[i]:
                return chr(i + ord('a'))
                
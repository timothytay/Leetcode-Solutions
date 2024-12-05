class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counts = [0] * 3
        for char in s:
            counts[ord(char) - ord('a')] += 1
        for count in counts:
            if count < k:
                return -1
        l = 0
        maxWindow = 0
        for r in range(len(s)):
            counts[ord(s[r]) - ord('a')] -= 1
            for i in range(len(counts)):
                while counts[i] < k:
                    counts[ord(s[l]) - ord('a')] += 1
                    l += 1
            maxWindow = max(maxWindow, r - l + 1)
        
        return len(s) - maxWindow
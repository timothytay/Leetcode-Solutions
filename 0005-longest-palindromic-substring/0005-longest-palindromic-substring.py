class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0

        for i in range(len(s)-1):
            for j in range(2):
                l, r = i, i+j
                if s[l] == s[r]:
                    
                    while l - 1 >= 0 and r + 1 < len(s) and s[l-1] == s[r+1]:
                        l -= 1
                        r += 1
                    if r - l > end - start:
                        start, end = l, r

        return s[start:end+1]
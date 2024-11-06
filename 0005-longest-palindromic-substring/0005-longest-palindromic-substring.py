class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, 0
        def getMax(l, r):
            if l - 1 < 0 or r + 1 >= len(s):
                return l, r
            if s[l-1] == s[r+1]:              
                return getMax(l-1, r+1)
            return l, r
            

        for i in range(len(s)):
            l, r = getMax(i, i)
            if r - l > right - left:
                right, left = r, l
            if i + 1 < len(s) and s[i] == s[i+1]:
                l, r = getMax(i, i+1)
                if r - l > right - left:
                    right, left = r, l

        return s[left:right+1]

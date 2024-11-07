class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        for i in range(len(s)):
            for j in range(2 if i + 1 < len(s) else 1):
                l, r = i, i+j
                if l == r or s[l] == s[r]:
                    while s[l] == s[r]:
                        count += 1
                        if l - 1 >= 0 and r + 1 < len(s):
                            l -= 1
                            r += 1
                        else:
                            break
        return count

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {}

        def decode(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return 1
            if s[start] == '0':
                return 0
            total = decode(start+1)
            if start + 1 < len(s) and int(s[start:start+2]) in range(10, 27):
                total += decode(start+2)
            memo[start] = total
            return memo[start]

        return decode(0)
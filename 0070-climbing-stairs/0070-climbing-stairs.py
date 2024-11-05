class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        memo = {}
        def climb(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = climb(n-1) + climb(n-2)
            return memo[n]

        return climb(n)
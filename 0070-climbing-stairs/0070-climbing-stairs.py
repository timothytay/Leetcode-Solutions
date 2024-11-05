class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [0, 0]
        dp[1] = 1
        dp[0] = 1
        counter = n - 2
        while counter >= 0:
            tmp = dp[0]
            dp[0] = dp[1] + dp[0]
            dp[1] = tmp

            counter -= 1
        return dp[0]
        

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(1, len(dp)):
            if dp[i] > 0:
                continue
            for coin in coins:
                if i - coin >= 0 and dp[i-coin] == -1:
                    continue
                elif i - coin >= 0 and (1 + dp[i - coin] < dp[i] or dp[i] == -1) and dp[i - coin] >= 0:
                    dp[i] = 1 + dp[i - coin]
            
        return dp[-1] 
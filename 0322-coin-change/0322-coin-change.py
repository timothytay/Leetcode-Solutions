from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def count(amountLeft):
            if amountLeft < 0:
                return -1
            if amountLeft == 0:
                return 0
            minCoinCount = float('inf')
            for coin in coins:
                coinCount = count(amountLeft - coin)
                if coinCount >= 0:
                    minCoinCount = min(minCoinCount, coinCount)
            if minCoinCount == float('inf'):
                return -1
            return 1 + minCoinCount

            
        return count(amount)
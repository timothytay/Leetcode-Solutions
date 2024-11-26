class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        l = 0
        for r in range(len(prices)):
            if r > 0 and prices[r] < prices[r-1]:
                total += prices[r-1] - prices[l]
                l = r
            if r == len(prices) - 1:
                total += prices[r] - prices[l]
        return total


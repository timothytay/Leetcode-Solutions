class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        bestProfit = 0
        if len(prices) == 1:
            return 0
        l = 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            bestProfit = max(profit, bestProfit)
            while l + 1 < r and prices[l + 1] < prices[l]:
                l += 1
        return bestProfit
        


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
            if prices[r] < prices[l]:
                l = r
            profit = prices[r] - prices[l]
            bestProfit = max(profit, bestProfit)
            
        return bestProfit
        


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxProf = max(maxProf, prices[r]-prices[l])
        return maxProf
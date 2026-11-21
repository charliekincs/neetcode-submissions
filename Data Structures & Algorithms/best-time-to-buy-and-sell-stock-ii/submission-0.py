class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        for r in range(len(prices)):
            cur = prices[r] - prices[l]
            if cur > 0:
                profit += cur
                l = r
            if prices[l] > prices[r]:
                l = r
        
        return profit

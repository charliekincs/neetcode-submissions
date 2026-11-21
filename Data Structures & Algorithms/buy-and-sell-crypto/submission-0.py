class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        l = 0

        for r in range(1, len(prices)):
            cur_profit = prices[r] - prices[l]
            max_profit = max(max_profit, cur_profit)
            if prices[r] < prices[l]:
                l = r
        return max(max_profit, 0)
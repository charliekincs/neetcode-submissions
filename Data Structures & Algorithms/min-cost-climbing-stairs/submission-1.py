from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def dp(n):
            if n == 1:
                return cost[1]
            if n == 0:
                return cost[0]

            mn = min(dp(n - 1), dp(n - 2))
            return mn + cost[n] if n < len(cost) else mn
        
        return dp(len(cost))
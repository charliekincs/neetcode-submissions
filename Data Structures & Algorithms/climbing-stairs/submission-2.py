from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dp(n):
            if n == 2:
                return 2
            if n == 1:
                return 1

            return dp(n - 1) + dp(n - 2)
        
        return dp(n)
from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def dp(i, cur_sum):
            if cur_sum == amount:
                return 1
            if i == len(coins):
                return 0
            if coins[i] + cur_sum > amount:
                return dp(i + 1, cur_sum)
            return dp(i, cur_sum + coins[i]) + dp(i + 1, cur_sum)

            
        return dp(0, 0)

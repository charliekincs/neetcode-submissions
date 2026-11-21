class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # [0, 1, 2, 3, 4, 1, 2]
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                a = i - c
                if a >= 0:
                    dp[i] = min(dp[i], 1 + dp[a])
        return dp[-1] if dp[-1] != float('inf') else -1
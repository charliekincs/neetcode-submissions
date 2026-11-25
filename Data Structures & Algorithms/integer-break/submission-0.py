class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            dp[i] = 0 if i == n else i
            for j in range(1, i):
                dp[i] = max(dp[i - j] * dp[j], dp[i])
        print(dp)
        
        return dp[n]


# product(6) = 9
# product(7) = 12
# product(9) = max(product(9 - 2) * 2, product(9 - 3) * 3)
# R(i) = max(R(i - j) * j, R(i)), where j < i

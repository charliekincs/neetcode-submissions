class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        squares = []
        for i in range(n):
            cur = i**2
            if cur > n:
                break
            squares.append(cur)

        for i in range(1, n + 1):
            mn = float('inf')
            for square in squares:
                mn = min(mn, dp[i - square] + 1)
            
            dp[i] = mn

        return dp[n]
        
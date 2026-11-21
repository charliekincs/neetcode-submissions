class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        memo = [1] * (n + 1)
        memo[0] = 0
        memo[2] = 2
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[-1]
    # [0, 1, 2, 3, ]
    # [1,1,1,1], [2,2], [1,1,2], [2,1,1], [1,2,1]
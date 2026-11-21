class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * (len(cost) + 1)
        memo[0] = cost[0]
        memo[1] = cost[1]
        for i in range(2, len(cost) + 1):
            mn = min(memo[i - 1], memo[i - 2])
            memo[i] = mn + cost[i] if i < len(cost) else mn

        return memo[-1]

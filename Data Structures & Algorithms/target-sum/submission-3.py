class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        tot = sum(nums)
        if abs(target) > tot or (tot + target) % 2:
            return 0
        goal = (target + tot) // 2

        dp = [0] * (goal + 1)
        dp[0] = 1
        for num in nums:
            for i in range(goal, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[goal]

        
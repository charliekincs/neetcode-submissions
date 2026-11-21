class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1) # dp[target] is solution
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num < 0:
                    continue
                dp[i] += dp[i - num] if dp[i - num] != -1 else 0

        print(dp)
        return dp[-1]

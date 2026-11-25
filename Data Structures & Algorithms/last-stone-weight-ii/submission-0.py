class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        tot = sum(stones)

        target = tot // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for stone in stones:
            for i in range(target, stone - 1, -1):
                if dp[i - stone]:
                    dp[i] = True

        for i in range(target, -1, -1):
            if dp[i]:
                return tot - (i * 2)


                    
            

                
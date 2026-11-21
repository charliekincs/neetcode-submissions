class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
       # len(text1) x len(text2)
       # count = 0
       # R(r, c) = 1 + max(R(r - 1, c), R(r, c - 1)) if text1[r] == text2[c] else max(R(r - 1, c), R(r, c - 1))
        dp = [[0] * len(text1) for _ in range(len(text2))]
        
        for i in range(len(text2)):
            for j in range(len(text1)):
                if (j == 0 or i == 0) and text1[j] == text2[i]:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i - 1][j - 1] + 1 if text1[j] == text2[i] else max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]

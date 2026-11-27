class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            if s3[i - 1] != s1[i - 1]:
                break
            dp[0][i] = True
        for i in range(1, n + 1):
            if s3[i - 1] != s2[i - 1]:
                break
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if dp[i - 1][j] and s3[i + j - 1] == s2[i - 1]:
                    dp[i][j] = True
                if dp[i][j - 1] and s3[i + j - 1] == s1[j - 1]:
                    dp[i][j] = True


        return dp[-1][-1]
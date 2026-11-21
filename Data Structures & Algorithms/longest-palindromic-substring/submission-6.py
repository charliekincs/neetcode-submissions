
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # for i in range(len(s) - 1):
        #     dp[i][i] = True
        #     if s[i] == s[i + 1]:
        #         dp[i][i + 1] = True

        res_start = res_end = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]): # outer vals match and inner is palindrome
                    dp[i][j] = True
                    window = j - i + 1
                    if window > res_end - res_start + 1:
                        res_start, res_end = i, j
            
        return s[res_start : res_end + 1]
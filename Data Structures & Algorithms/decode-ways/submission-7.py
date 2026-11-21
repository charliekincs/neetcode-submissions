class Solution:
    def numDecodings(self, s: str) -> int:
        if s and s[0] == '0':
            return 0
       
        memo = [0] * (len(s) + 1)
        memo[0] = 1
        memo[1] = 1
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i - 2:i]) <= 26:
                memo[i] += memo[i - 2]
            if 1 <= int(s[i - 1]) <= 9:
                memo[i] += memo[i - 1]
        
        return memo[len(s)]




class Solution:
    def countSubstrings(self, s: str) -> int:
        if s == '':
            return 0

        memo = [0] * (len(s) + 1)
        for r in range(len(s)):
            count = 1
            for l in range(r):
                substr = s[l : r + 1]
                if substr == substr[::-1]:
                    count += 1
            memo[r + 1] = memo[r] + count
        return memo[-1]
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        frequencies = {}
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in frequencies and frequencies[s[r]] == 1:
                frequencies[s[l]] -= 1
                l += 1
            frequencies[s[r]] = 1
            res = max(res, r - l + 1)
        
        return res
        
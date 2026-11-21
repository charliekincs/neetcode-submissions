class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        indices = {s[0] : 0}
        l = 0
        max_substr = 1

        for r in range(1, len(s)):
            if s[r] in indices and indices[s[r]] >= l:
                l = indices[s[r]] + 1
            max_substr = max(max_substr, r-l+1)
            indices[s[r]] = r
        return max_substr
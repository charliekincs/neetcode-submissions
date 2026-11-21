class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices = {}
        l = 0
        max_substr = 0

        for r in range(len(s)):
            if s[r] in indices and indices[s[r]] >= l:
                l = indices[s[r]] + 1  # Move `l` to the right of the last occurrence

            indices[s[r]] = r  # Update the last seen index
            max_substr = max(max_substr, r - l + 1)  # Update max length

        return max_substr
class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l, r):
            count = 0
            while l > -1 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        found = 0
        for i in range(len(s)):
            found += expand(i, i)
            found += expand(i, i + 1)
        return found
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        max_count = 0
        res = 0
        l = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            max_count = max(max_count, counts[s[right]])

            while (right - l + 1) - max_count > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, (right - l + 1))
        
        return res
from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def canBreak(i):
            if i == len(s):
                return True
            
            return any(canBreak(j) for j in range(i, len(s) + 1) if s[i:j] in wordDict)
        
        return canBreak(0)
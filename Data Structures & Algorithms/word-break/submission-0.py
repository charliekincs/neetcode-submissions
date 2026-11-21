from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def canBreak(i):
            if i == len(s):
                return True
            
            return any(canBreak(j + 1) for j in range(i, len(s)) if s[i:j + 1] in wordDict)
        
        return canBreak(0)
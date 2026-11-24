from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)

        @cache
        def dp(i):
            if i == n:
                return True
            if i > n:
                return False
            
            for word in wordDict:
                if s[i: i + len(word)] == word and dp(i + len(word)):
                    return True
            return False

        return dp(0)


            
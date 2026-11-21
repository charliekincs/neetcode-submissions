class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []

        def backtrack(start):
            if start == len(s):
                res.append(sub.copy())
                return
            
            for end in range(start, len(s)):
                substring = s[start:end + 1]

                if substring == substring[::-1]:
                    sub.append(substring)
                    backtrack(end + 1)
                    sub.pop()
        
        backtrack(0)
        return res

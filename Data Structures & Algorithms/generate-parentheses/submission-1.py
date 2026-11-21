class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ''

        def backtrack(leftCount):
            nonlocal cur
            if len(cur) == n * 2:
                res.append(cur)
                return
            if leftCount == n:
                cur += ')'
                backtrack(leftCount)
                cur = cur[:-1]
                return
            
            cur += '('
            backtrack(leftCount + 1)
            cur = cur[:-1]
            if leftCount > len(cur) - leftCount:
                cur += ')'
                backtrack(leftCount)
                cur = cur[:-1]

        
        backtrack(0)
        return res
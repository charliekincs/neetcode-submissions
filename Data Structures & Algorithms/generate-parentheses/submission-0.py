class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        parens = ''

        def backtrack(leftCount):
            nonlocal parens
            if len(parens) == n * 2:
                res.append(parens)
                return
            if leftCount == n:
                parens += ')'
                backtrack(leftCount)
                parens = parens[:-1]
                return
            
            parens += '('
            backtrack(leftCount + 1)
            parens = parens[:-1]
            if leftCount > len(parens) - leftCount:
                parens += ')'
                backtrack(leftCount)
                parens = parens[:-1]
        
        backtrack(0)
        return res
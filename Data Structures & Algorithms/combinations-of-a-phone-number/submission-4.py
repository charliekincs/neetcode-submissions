class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        mappings = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        cur = ''

        def backtrack(i):
            nonlocal cur
            if i == len(digits):
                res.append(cur)
                # cur = cur[:-1]
                return

            for char in mappings[digits[i]]:
                cur += char
                backtrack(i + 1)
                cur = cur[:-1]
            
        
        backtrack(0)
        return res

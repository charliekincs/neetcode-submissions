class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        output = []

        def backtrack(s):
            if len(s) == len(digits):
                output.append(s[:])
                return
            
            mapping = digitToChar[digits[len(s)]]
            for i in range(len(mapping)):
                s += mapping[i]
                backtrack(s)
                s = s[:-1]
        
        backtrack('')
        return output

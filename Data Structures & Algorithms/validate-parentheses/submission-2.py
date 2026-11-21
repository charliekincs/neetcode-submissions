class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding = {
            "{": "}",
            "[": "]", 
            "(": ")",
            "}": "{",
            "]": "[", 
            ")": "("
        }
        right = set(["}", "]", ")"])
        left = set(["{", "[", "("])

        for ch in s:
            if ch in left:
                stack.append(ch)
            elif ch in right and stack != []:
                r = stack.pop()
                if ch != corresponding[r]:
                    return False
            else:
                return False

        if stack != []:
            return False 
        return True
            
        
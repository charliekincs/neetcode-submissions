class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(start):
            if start == len(s):
                res.append(path.copy())
                return

            for end in range(start, len(s)):
                substr = s[start : end + 1]

                if substr == substr[::-1]:
                    path.append(substr)
                    backtrack(end + 1)
                    path.pop()


        backtrack(0)
        return res
        
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combo = []
        curSum = 0

        def backtrack(i):
            nonlocal curSum
            if curSum == target:
                res.append(combo.copy())
                return

            for j in range(i, len(candidates)):
                potential = candidates[j]
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                    
                if potential + curSum > target:
                    break
                combo.append(potential)
                curSum += potential
                backtrack(j + 1)
                combo.pop()
                curSum -= potential


        backtrack(0)
        return res

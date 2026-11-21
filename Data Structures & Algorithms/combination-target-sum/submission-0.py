class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        def backtrack(start, curSum):
            if curSum == target:
                res.append(combo.copy())
                return
            if curSum > target:
                return
            
            for i in range(start, len(nums)):
                combo.append(nums[i])
                curSum += nums[i]

                backtrack(i, curSum)

                combo.pop()
                curSum -= nums[i]
        
        backtrack(0, 0)
        return res
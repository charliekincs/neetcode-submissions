class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        curSum = 0

        def backtrack(start):
            nonlocal curSum
            if curSum == target:
                res.append(cur.copy())
                return
            if curSum > target:
                return

            for pos in range(start, len(nums)):
                cur.append(nums[pos])
                curSum += nums[pos]
                backtrack(pos)
                cur.pop()
                curSum -= nums[pos]

        
        backtrack(0)
        return res
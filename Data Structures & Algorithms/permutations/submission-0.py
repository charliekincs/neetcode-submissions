class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        def backtrack(i):
            if i == len(nums) and len(perm) == len(nums) and len(set(perm)) == len(perm):
                res.append(perm.copy())
                return
            if i == len(nums) and len(perm) != len(nums) or len(set(perm)) != len(perm):
                return
            
            for num in nums:
                perm.append(num)
                backtrack(i + 1)
                perm.pop()
                backtrack(i + 1)

        backtrack(0)
        return res
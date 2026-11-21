class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(num for num in nums)
        
        starters = [num for num in numsSet if num - 1 not in numsSet]
        res = 0
        for starter in starters:
            cur = starter
            curCount = 1
            while cur + 1 in numsSet:
                curCount += 1
                cur += 1
            res = max(res, curCount)

        return res


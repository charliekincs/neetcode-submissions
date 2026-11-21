class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        processed = set()
        res = 0
        for num in numsSet:
            if num in numsSet and num - 1 not in numsSet:
                cur = num
                curCount = 0
                while cur in numsSet and cur not in processed:
                    curCount += 1
                    processed.add(cur)
                    cur += 1
                res = max(res, curCount)

        return res 

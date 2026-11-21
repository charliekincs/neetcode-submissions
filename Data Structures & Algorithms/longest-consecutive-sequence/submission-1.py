class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums) 

        maxSeq = 0
        for num in nums:
            if num - 1 in numsSet:
                continue
            
            curSeq = 1
            curNum = num + 1
            while curNum in numsSet:
                curSeq += 1
                curNum += 1
            
            maxSeq = max(maxSeq, curSeq)
        return maxSeq
    
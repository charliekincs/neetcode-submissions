class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSet = set()
        for num in nums:
            numsSet.add(num)
        
        for num in range(len(nums) + 1):
            if num not in numsSet:
                return num
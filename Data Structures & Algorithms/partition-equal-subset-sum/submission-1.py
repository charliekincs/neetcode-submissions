class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2
        nums_set = set([0])
        for num in nums:
            if target - num in nums_set:
                return True
            for cached in list(nums_set):
                nums_set.add(num + cached)
            nums_set.add(num)

        return False


      
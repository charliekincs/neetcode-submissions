class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
        
        target = total / 2

        def dp(i, cur_sum):
            if cur_sum == target:
                return True
            if i == len(nums):
                return False
            
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                if dp(j + 1, cur_sum):
                    return True
                cur_sum -= nums[j]
            return False
        
        return dp(0, 0)

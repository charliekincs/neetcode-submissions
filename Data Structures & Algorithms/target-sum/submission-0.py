from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(i, cur_sum):
            if i == len(nums):
                return 1 if cur_sum == target else 0
            
            return dp(i + 1, cur_sum - nums[i]) + dp(i + 1, cur_sum + nums[i])
        
        return dp(0, 0)
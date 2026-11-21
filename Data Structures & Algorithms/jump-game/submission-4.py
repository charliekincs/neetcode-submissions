class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        n = len(nums) - 1
        prev = float('inf')
        for i in range(len(nums) - 2, -1, -1):
            land = i + nums[i]
            if land >= n or land >= prev:
                prev = i
          
        return prev == 0
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        cur = 1
        output[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            cur = cur * nums[i + 1]
            output[i] = cur
        
        cur = 1
        for i in range(len(nums)):
            output[i] *= cur
            cur = cur * nums[i]
        
        return output

        
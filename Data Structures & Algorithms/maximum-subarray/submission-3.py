class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curSum = 0

        for num in nums:
            curSum = curSum + num if curSum + num > num else num
            res = max(res, curSum)

        return res

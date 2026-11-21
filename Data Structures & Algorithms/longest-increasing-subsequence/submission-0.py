class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    L[i] = max(L[i], L[j] + 1)
        return max(L)



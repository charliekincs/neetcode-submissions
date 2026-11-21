class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curSum = nums[l] + nums[r]
                target = -nums[i]
                if curSum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < len(nums) - 1 and nums[l + 1] == nums[l]:
                        l += 1
                if curSum > target:
                    r -= 1
                else:
                    l += 1
        return res
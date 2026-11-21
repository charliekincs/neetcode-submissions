class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for pos in range(len(nums)):
            if pos > 0 and nums[pos] == nums[pos - 1]:
                continue
            l = pos + 1
            r = len(nums) - 1
            while l < r:
                curSum = nums[pos] + nums[l] + nums[r]
                if curSum == 0:
                    triplets.append([nums[pos], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif curSum > 0:
                    r -= 1
                else:
                    l += 1
        
        return triplets
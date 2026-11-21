class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            prev_idx = l - 1 if l > 0 else -1
            if nums[l] < nums[prev_idx]:
                return nums[l]
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]

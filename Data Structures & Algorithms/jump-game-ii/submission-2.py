class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums) - 1
        l = r = 0
        jumps = 0
        while r < N:
            farthest = r + 1
            for i in range(l, r + 1):
                r = max(r, i + nums[i])
            l = farthest
            jumps += 1

        return jumps



        
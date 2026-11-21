class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        trips = set()
        for i in range(len(nums)):
            cur = nums[i]
            cur_nums = set()
            for j in range(i + 1, len(nums)):
                target = -(nums[j] + cur)
                trip = str(nums[j]) + str(cur) + str(target)
                trip = str(sorted(trip))
                if target in cur_nums and trip not in trips:
                    res.append([nums[j], cur, target])
                    trips.add(trip)
                cur_nums.add(nums[j])
        return res
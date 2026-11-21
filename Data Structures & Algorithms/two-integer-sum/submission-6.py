class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}

        for idx, num in enumerate(nums):
            idxs[num] = idx
        
        for idx, num in enumerate(nums): 
            remaining = target - num
            if remaining in idxs and idx != idxs[remaining]:
                return [idxs[remaining], idx] if idx > idxs[remaining] else [idx, idxs[remaining]]

        return []

        
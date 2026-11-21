class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        cur = -1
        while k > 0:
            cur = heapq.heappop_max(nums)
            k -= 1
        return cur

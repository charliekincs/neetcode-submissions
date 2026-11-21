class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(nums[i], i) for i in range(k)]
        heapq.heapify_max(heap)
        res = []
        l, r = 0, k - 1
        while r < len(nums):
            while heap[0][1] < l:
                heapq.heappop_max(heap)
            cur, idx = heap[0] # use the max
            res.append(cur)
            l += 1
            r += 1
            if r < len(nums):
                heapq.heappush_max(heap, (nums[r], r))

        return res
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p1, p2 in points:
            euclidean = math.sqrt((0 - p1)**2 + (0 - p2)**2)
            heapq.heappush_max(heap, (euclidean, p1, p2))

            if len(heap) > k:
                heapq.heappop_max(heap)

        return [[p1, p2] for euc, p1, p2 in heap]




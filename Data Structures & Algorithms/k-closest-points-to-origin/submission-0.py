import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p1, p2 in points:
            euclidean = math.sqrt((0 - p1)**2 + (0 - p2)**2)
            heapq.heappush(heap, (euclidean, p1, p2))
        
        res = []
        while k > 0:
            point = heapq.heappop(heap)
            res.append([point[1], point[2]])
            k -= 1

        return res
        
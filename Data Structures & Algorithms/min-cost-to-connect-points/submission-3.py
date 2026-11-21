class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, points[0])]
        mst = set()

        totalCost = 0
        while heap:
            cost, node = heapq.heappop(heap)

            if tuple(node) in mst:
                continue
            mst.add(tuple(node))
            totalCost += cost
            for p1, p2 in points:
                if (p1, p2) in mst or [p1, p2] == node:
                    continue
                manhattan = abs(p1 - node[0]) + abs(p2 - node[1])
                heapq.heappush(heap, (manhattan, [p1, p2]))

        return totalCost
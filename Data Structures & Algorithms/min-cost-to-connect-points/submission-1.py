class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_cost = {}
        for point in points:
            min_cost[tuple(point)] = float('inf')
        
        min_cost[tuple([points[0][0], points[0][1]])] = 0
        q = [(0, points[0][0], points[0][1])]
        mst = set()
        total_cost = 0
        while q:
            cost, pointx, pointy = heapq.heappop(q)

            t = tuple([pointx, pointy])
            if cost > min_cost[t] or t in mst:
                continue
            mst.add(t)
            total_cost += cost
            for nei_point in points:
                if nei_point == [pointx, pointy]:
                    continue
                manhattan = abs(nei_point[0] - pointx) + abs(nei_point[1] - pointy)
                nei_t = tuple([nei_point[0], nei_point[1]])
                if manhattan < min_cost[nei_t]:
                    min_cost[nei_t] = manhattan
                    heapq.heappush(q, (manhattan, nei_t[0], nei_t[1]))
        
        return total_cost
                    




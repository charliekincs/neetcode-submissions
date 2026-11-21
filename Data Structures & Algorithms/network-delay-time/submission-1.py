class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(set)
        for ui, vi, ti in times:
            adj[ui].add((vi, ti))
        
        dist = {k : 0}
        heap = [(0, k)]
        heapq.heapify(heap)
        while heap:
            cur_time, cur_node = heapq.heappop(heap)

            neighbors = adj.get(cur_node)
            if neighbors is None:
                continue
            for nei_node, nei_time in neighbors:
                new_time = cur_time + nei_time
                if dist.get(nei_node) is None or new_time < dist.get(nei_node):
                    dist[nei_node] = new_time
                    heapq.heappush(heap, (new_time, nei_node))

        if len(dist) == n:
            return max(dist.values())

        return -1
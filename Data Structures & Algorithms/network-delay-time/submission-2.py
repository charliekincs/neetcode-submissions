class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(set)
        for src, dst, t in times:
            adj[src].add((dst, t))

        dist = {k: 0}
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)

            for nei, t in adj[node]:
                new_time = time + t
                if nei not in dist or new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap, (new_time, nei))

        return max(dist.values()) if len(dist) == n else -1
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(set)

        for time in times:
            graph[time[0]].add((time[1], time[2]))
        
        dist = {k: 0}

        heap = [(0, k)]

        while heap:
            count, node = heapq.heappop(heap)

            if dist[node] < count:
                continue

            for neighbor, neighbor_time in graph[node]:
                neighbor_count = count + neighbor_time

                if neighbor not in dist or neighbor_count < dist[neighbor]:
                    dist[neighbor] = neighbor_count
                    heapq.heappush(heap, (neighbor_count, neighbor))
            
        if len(dist) != n:
            return -1
        
        return max(dist.values())





        
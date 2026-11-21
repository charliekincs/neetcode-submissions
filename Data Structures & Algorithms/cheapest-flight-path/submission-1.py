class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(set)
        for s, d, p in flights:
            adj[s].add((d, p))

        heap = [(0, src, 0)]
        prices = {(src, 0) : 0}

        while heap:
            cur_price, cur_node, cur_flights = heapq.heappop(heap)
            if cur_flights > k + 1 or cur_price > prices[(cur_node, cur_flights)]:
                continue

            for nei, nei_price in adj[cur_node]:
                new_price = cur_price + nei_price
                flights = cur_flights + 1
                if flights > k + 1:
                    continue
                if (nei, flights) not in prices or prices[(nei, flights)] > new_price:
                    prices[(nei, flights)] = new_price
                    heapq.heappush(heap, (new_price, nei, flights))

        res = float('inf')
        for (node, flights), price in prices.items():
            if node == dst:
                res = min(res, price)

        return res if res != float('inf') else -1
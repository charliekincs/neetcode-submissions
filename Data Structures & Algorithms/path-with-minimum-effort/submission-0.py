class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0, 0)] # effort, r, c

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visit = set()
        while heap:
            effort, r, c = heapq.heappop(heap)
            if r == len(heights) - 1 and c == len(heights[r]) - 1:
                return effort

            if (r, c) in visit:
                continue

            visit.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(heights) and 0 <= nc < len(heights[nr]):
                    newEffort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    heapq.heappush(heap, (newEffort, nr, nc))


        return 0

        

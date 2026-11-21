class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0, 0)] # effort, row, col
        dist = {(0, 0): 0}

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while heap:
            effort, row, col = heapq.heappop(heap)

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if new_row in (-1, len(heights)) or new_col in (-1, len(heights[0])):
                    continue
                diff = max(effort, abs(heights[new_row][new_col] - heights[row][col]))
                t = (new_row, new_col)
                if t not in dist or (t in dist and diff < dist[t]):
                    dist[t] = diff
                    heapq.heappush(heap, (diff, new_row, new_col))


        return dist[(len(heights) - 1, len(heights[0]) - 1)]

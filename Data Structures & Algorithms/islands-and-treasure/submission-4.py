from collections import deque

class Solution:
    INF = 2147483647
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))

        path = set()
        q = deque(q)
        while q:
            cur_row, cur_col, dist = q.popleft()

            for dr, dc in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                nei_row = cur_row + dr
                nei_col = cur_col + dc
                if nei_row < 0 or nei_col < 0 or nei_row > len(grid) - 1 or nei_col > len(grid[nei_row]) - 1:
                    continue
                if (nei_row, nei_col) in path or grid[nei_row][nei_col] == -1:
                    continue
                if grid[nei_row][nei_col] == self.INF:
                    grid[nei_row][nei_col] = dist + 1
                path.add((nei_row, nei_col))
                q.append((nei_row, nei_col, dist + 1))


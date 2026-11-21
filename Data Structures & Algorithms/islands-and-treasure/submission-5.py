class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dist = 0
        while q:
            dist += 1
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if new_row in (-1, len(grid)) or new_col in (-1, len(grid[0])):
                        continue
                    if grid[new_row][new_col] != INF:
                        continue
                    
                    grid[new_row][new_col] = dist
                    q.append((new_row, new_col))
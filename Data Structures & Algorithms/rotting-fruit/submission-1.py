class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                   q.append((i, j))

        minutes = 0
        while q:
            spread = False
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_row = row + dr
                    new_col = col + dc
                    if new_row in [-1, len(grid)] or new_col in [-1, len(grid[new_row])]:
                        continue
                    if grid[new_row][new_col] != 1:
                        continue
                    grid[new_row][new_col] = 2
                    q.append((new_row, new_col))
                    spread = True
            if spread:
                minutes += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return minutes

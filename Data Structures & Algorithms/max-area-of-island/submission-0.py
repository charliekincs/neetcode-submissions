class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def bfs(row, col):
            if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[row]) - 1:
                return
            if grid[row][col] == 0:
                return
            if (row, col) in visited:
                return
            
            visited.add((row, col))
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_r = row + dr
                new_c = col + dc
                if (new_r, new_c) not in visited:
                    bfs(new_r, new_c)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited:
                    before_size = len(visited)
                    bfs(i, j)
                    after_size = len(visited) - before_size
                    res = max(res, after_size)

        return res

                
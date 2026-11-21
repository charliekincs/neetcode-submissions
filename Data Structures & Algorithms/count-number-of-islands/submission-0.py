class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        def dfs(row, col):
            if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1:
                return
            if grid[row][col] == '0':
                return
            if (row, col) in visited:
                return
            
            visited.add((row, col))

            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                dfs(row + dr, col + dc)


        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1
        
        return islands
        
            
        
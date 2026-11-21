class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific_visited = set()
        atlantic_visited = set()
        def bfs(row, col, visited):
            if row < 0 or col < 0 or row > len(heights) - 1 or col > len(heights[row]) - 1:
                return
            if ((row, col)) in visited:
                return
            
            visited.add((row, col))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nei_row = row + dr
                nei_col = col + dc
                if nei_row >= 0 and nei_col >= 0 and nei_row <= len(heights) - 1 and nei_col <= len(heights[row]) - 1:
                    if heights[nei_row][nei_col] >= heights[row][col]:
                        bfs(nei_row, nei_col, visited)
            
        for i in range(len(heights)):
            bfs(i, 0, pacific_visited)
            bfs(i, len(heights[0]) - 1, atlantic_visited)

        for i in range(len(heights[0])):
            bfs(0, i, pacific_visited)
            bfs(len(heights) - 1, i, atlantic_visited)

        return list(pacific_visited & atlantic_visited)
        
            

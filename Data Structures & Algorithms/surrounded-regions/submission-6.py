from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()

        def bfs(i, j):
            q = deque([(i, j)])
            while q:
                row, col = q.popleft()

                if board[row][col] == 'X' or (row, col) in visited:
                    continue
                
                visited.add((row, col))
                for dr, dc in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                    nei_row = row + dr
                    nei_col = col + dc
                    if nei_row < 0 or nei_col < 0 or nei_row > len(board) - 1 or nei_col > len(board[nei_row]) - 1:
                        continue
                    q.append((nei_row, nei_col))

            

        for i in range(len(board)):
            bfs(i, 0)
            bfs(i, len(board[i]) - 1)

        for i in range(len(board[0])):
            bfs(0, i)
            bfs(len(board) - 1, i)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i, j) not in visited and board[i][j] == 'O':
                    board[i][j] = 'X'


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()

        def search(row, col, curWord):
            if row > len(board) - 1 or row < 0:
                return False
            if col > len(board[row]) - 1 or col < 0:
                return False
            if (row, col) in visited:
                return False
            
            if board[row][col] != word[len(curWord)]:
                return False
            curWord += board[row][col]
            visited.add((row, col))
            if curWord == word:
                return True

            res = (search(row + 1, col, curWord) or search(row - 1, col, curWord) or search(row, col + 1, curWord) or search(row, col - 1, curWord))

            visited.remove((row, col))
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if search(i, j, ""):
                        return True
        return False
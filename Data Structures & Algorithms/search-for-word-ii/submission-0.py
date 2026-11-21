class TrieNode:
    def __init__(self):
        self.children = {}
        self.isCompleteWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.isCompleteWord = True

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visit = set()
        res = []
        def dfs(row, col, s, cur):
            if row in (-1, len(board)) or col in (-1, len(board[0])) or (row, col) in visit:
                return
            if board[row][col] not in cur.children:
                return

            visit.add((row, col))
            s += board[row][col]
            cur = cur.children[board[row][col]]
            if cur.isCompleteWord:
                res.append(s)
                cur.isCompleteWord = False # so it can't be re-added to res
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                dfs(new_row, new_col, s, cur)
            visit.remove((row, col))

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in root.children:
                    dfs(i, j, '', root)
        
        return res


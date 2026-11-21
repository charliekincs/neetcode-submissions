class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_adj = defaultdict(list)
        col_adj = defaultdict(list)
        for above, below in rowConditions:
            row_adj[above].append(below)
        
        for left, right in colConditions:
            col_adj[left].append(right)
    
        def topo(node, visited, path, adj, ordering):
            if node in path:
                return False
            if node in visited:
                return True
            path.add(node)
            visited.add(node)
            for nei in adj[node]:
                if not topo(nei, visited, path, adj, ordering):
                    return False
            ordering.append(node)
            path.remove(node)
            return True

        row_ordering = []
        col_ordering = []
        row_visited = set()
        col_visited = set()
        for i in range(1, k + 1):
            if not topo(i, row_visited, set(), row_adj, row_ordering):
                return []
            if not topo(i, col_visited, set(), col_adj, col_ordering):
                return []
        
        row_ordering.reverse()
        col_ordering.reverse()
        row_cords = {}
        col_cords = {}
        for i in range(k):
            row_cords[row_ordering[i]] = i
            col_cords[col_ordering[i]] = i
        
        res = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            row = row_cords[i]
            col = col_cords[i]
            res[row][col] = i

        return res




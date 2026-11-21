class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_adj = defaultdict(list)
        col_adj = defaultdict(list)
        row_indegree = [0] * (k + 1)
        col_indegree = [0] * (k + 1)
        for above, below in rowConditions:
            row_adj[above].append(below)
            row_indegree[below] += 1
        
        for left, right in colConditions:
            col_adj[left].append(right)
            col_indegree[right] += 1
    
        def topo(adj, indegree, ordering):
            q = deque()
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    q.append(i)
            while q:
                cur = q.popleft()
                ordering.append(cur)
                for nei in adj[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            return len(ordering) == k


        row_ordering = []
        col_ordering = []
        if not topo(row_adj, row_indegree, row_ordering):
            return []
        if not topo(col_adj, col_indegree, col_ordering):
            return []
        
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




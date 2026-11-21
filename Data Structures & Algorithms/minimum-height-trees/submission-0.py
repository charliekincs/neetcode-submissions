class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for n1, n2 in edges:
            adj[n1].add(n2)
            adj[n2].add(n1)
        
        def dfs(parent, node):
            best = 0
            for nei in adj[node]:
                if nei != parent:
                    best = max(best, 1 + dfs(node, nei))
            return best

        res = []
        minHeight = float('inf')
        for i in range(n):
            best = dfs(-1, i)
            if res and best < minHeight:
                res = [i]
                minHeight = best
            elif res and best == minHeight:
                res.append(i)
            elif not res:
                res.append(i)
                minHeight = best
        return res
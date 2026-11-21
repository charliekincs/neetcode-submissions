class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for v1, v2 in edges:
            adj[v1].add(v2)
            adj[v2].add(v1)
        
        redundant_edges = set()
        def dfs(node, parent, path):
            if node in path:
                return False
            
            path.add(node)
            neighbors = adj.get(node)
            if neighbors is None:
                return
            for nei in neighbors:
                if nei != parent and not dfs(nei, node, path):
                    redundant_edges.add(tuple([min(node, nei), max(node, nei)]))
                    return False
            
            return True


        dfs(edges[0][0], edges[0][0], set())
        for i in range(len(edges) - 1, -1, -1):
            if tuple(edges[i]) in redundant_edges:
                return edges[i]
        
        return []
        
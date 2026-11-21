class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for node1, node2 in edges:
            adj[node1].add(node2)
            adj[node2].add(node1)
        
        visited = set()

        def bfs(node):
            if node in visited:
                return
            
            visited.add(node)
            neighbors = adj.get(node)
            if neighbors is None:
                return
            for neighbor in neighbors:
                bfs(neighbor)

        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                bfs(node)
        
        return count
        
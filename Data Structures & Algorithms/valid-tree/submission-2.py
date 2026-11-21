class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for node1, node2 in edges:
            adj[node1].add(node2)
            adj[node2].add(node1)
        
        visited = set()
        def search(node, parent):
            neighbors = adj.get(node)
            if node in visited:
                return False
            
            visited.add(node)
            if neighbors is None:
                return True
            for nei in neighbors:
                if nei != parent:
                    if not search(nei, node):
                        return False
            
            return True
            
        for i in range(n):
            if i in visited:
                continue
            if not search(i, i):
                return False
            if len(visited) < n:
                return False

            
        return True

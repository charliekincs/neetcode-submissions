class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for node1, node2 in edges:
            adj[node1].add(node2)
            adj[node2].add(node1)
        
        visited = set()
        def search(node, parent):
            if node in visited:
                return
            visited.add(node)
            neighbors = adj.get(node)
            if neighbors is None or (len(neighbors) == 1 and parent in neighbors):
                return
            for nei in neighbors:
                if nei != parent:
                    search(nei, node)

        res = 0
        for i in range(n):
            if i not in visited:
                search(i, i)
                res += 1
        return res
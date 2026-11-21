class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for n1, n2 in edges:
            adj[n1].add(n2)
            adj[n2].add(n1)
        
        visited = set()
        cycle_start = -1
        cycle = set()
        def dfs(parent, node):
            nonlocal cycle_start
            if node in visited:
                cycle_start = node
                return False

            visited.add(node)
            for nei in adj[node]:
                if nei != parent:
                    if not dfs(node, nei):
                        if cycle_start != -1:
                            cycle.add(node)
                        if node == cycle_start:
                            cycle_start = -1
                        return False
            return True
        
        dfs(1, 1)
        for n1, n2 in reversed(edges):
            if n1 in cycle and n2 in cycle:
                return [n1, n2]

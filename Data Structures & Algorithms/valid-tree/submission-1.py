class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for edge in edges: 
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        
        start_node = 0
        visited = set([start_node])
        q = [(start_node, -1)]
        while q:
            node, parent = q.pop(0)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                q.append((neighbor, node))
        
        if len(visited) != n:
            return False
        return True

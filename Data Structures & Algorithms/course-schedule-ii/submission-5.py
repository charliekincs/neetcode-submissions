class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for course, prereq in prerequisites:
            adj[course].add(prereq)
        
        visited = set()
        ordering = []
        def dfs(node, path):
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)
            visited.add(node)
            for nei in adj[node]:
                if not dfs(nei, path):
                    return False
            ordering.append(node)
            path.remove(node)
            return True
        
        for node in range(numCourses):
            if node not in visited and not dfs(node, set()):
                return []
        return ordering
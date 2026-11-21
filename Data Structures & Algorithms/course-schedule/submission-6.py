class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True
        adj = defaultdict(set)
        for course, prereq in prerequisites:
            adj[course].add(prereq)
        
        visited = set()
        def dfs(node, path):
            if node in visited:
                return True
            if node in path:
                return False
            path.add(node)
            neighbors = adj.get(node)
            if neighbors is None:
                visited.add(node)
                path.remove(node)
                return True
            for nei in neighbors:
                if not dfs(nei, path):
                    return False
            visited.add(node)
            path.remove(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course, set()):
                return False

        return True
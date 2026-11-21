class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for course, prereq in prerequisites:
            adj[course].add(prereq)
        
        visited = set()
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
            path.remove(node)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i, set()):
                    return False

        return True
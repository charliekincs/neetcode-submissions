class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(set)

        for prerequisite in prerequisites:
            course, prereq = prerequisite
            prereq_map[course].add(prereq)

        visited = set()
        def dfs(node, path):
            if node in visited:
                return True
            if node in path:
                return False
            neighbors = prereq_map.get(node)
            if not neighbors:
                return True
            
            path.add(node)
            for neighbor in prereq_map[node]:
                if not dfs(neighbor, path):
                    return False
            path.remove(node)
            visited.add(node)
            return True
        
        for course, prereqs in prereq_map.items():
            if course in visited:
                continue
            path = set()
            if not dfs(course, path):
                return False
            
        return True

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        for prereq, course in prerequisites:
            adj[course].add(prereq)
        
        visit = set()
        prereqs = [set() for _ in range(numCourses)]
        def dfs(node):
            if node in visit:
                return prereqs[node]

            visit.add(node)
            for nei in adj[node]:
                prereqs[node] |= dfs(nei)
                prereqs[node].add(nei)
            return prereqs[node]
        
        for i in range(numCourses):
            if i not in visit:
                dfs(i)

        res = []
        for prereq, course in queries:
            res.append(prereq in prereqs[course])
        
        return res

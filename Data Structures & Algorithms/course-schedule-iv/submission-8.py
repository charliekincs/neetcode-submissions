class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        indegrees = [0] * numCourses
        for prereq, course in prerequisites:
            adj[prereq].add(course)
            indegrees[course] += 1
        
        prereqs = [set() for _ in range(numCourses)]
        q = deque([course for course in range(numCourses) if indegrees[course] == 0])
        while q:
            cur = q.popleft()

            for nei in adj[cur]:
                prereqs[nei].add(cur)
                prereqs[nei] |= prereqs[cur]
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)

        res = []
        for prereq, course in queries:
            res.append(prereq in prereqs[course])
        return res

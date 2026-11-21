class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = {course: 0 for course in range(numCourses)}
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegrees[course] = 1 + indegrees.get(course, 0)

        
        q = deque([node for node, indegree in indegrees.items() if indegree == 0])

        ordering = []
        while q:
            cur = q.popleft()

            ordering.append(cur)
            for nei in adj[cur]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)

        print(ordering)
        return ordering if len(ordering) == numCourses else []
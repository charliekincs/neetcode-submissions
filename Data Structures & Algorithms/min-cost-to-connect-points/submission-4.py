class Solution:

    rank = {}
    parent = {}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node] # the node whose parent is itself gets assigned as parent for every node up the chain

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return False
        
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        return True

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for point in points:
            t = tuple(point)
            self.parent[t] = t
            self.rank[t] = 1
            for nei in points:
                if point == nei:
                    continue
                nei_x, nei_y = nei
                p_x, p_y = point
                manhattan = abs(nei_y - p_y) + abs(nei_x - p_x)
                edges.append((manhattan, point, nei))
        
        edges.sort()

        total = 0
        for edge in edges:
            n1, n2 = tuple(edge[1]), tuple(edge[2])
            if self.union(n1, n2):
                total += edge[0]
        
        return total


        

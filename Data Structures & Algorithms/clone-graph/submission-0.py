"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        visited = {node.val: Node(node.val)}

        q = [node]
        while q:
            cur = q.pop(0)

            new = visited[cur.val]
            for neighbor in cur.neighbors:
                if neighbor.val not in visited:
                    this = Node(neighbor.val)
                    visited[neighbor.val] = this
                    q.append(neighbor)
                
                new.neighbors.append(visited[neighbor.val])

        return visited[node.val]
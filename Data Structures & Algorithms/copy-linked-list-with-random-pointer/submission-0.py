"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        new_head = Node(head.val)
        new_cur = new_head
        cur = head
        copies = {cur: new_cur}
        while cur:
            new_cur.next = Node(cur.next.val) if cur.next else None
            new_cur = new_cur.next
            cur = cur.next
            if cur:
                copies[cur] = new_cur

        cur = head
        while cur:
            copies[cur].random = copies[cur.random] if cur.random else None
            cur = cur.next
            

        return new_head

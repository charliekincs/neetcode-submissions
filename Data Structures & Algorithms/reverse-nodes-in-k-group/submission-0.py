# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        
        num_groups = cnt // k

        def rev(node, group_count):
            if not node:
                return None
            if group_count >= num_groups:
                return node
            prev = None
            group_tail = node # head of group will become tail
            for _ in range(k):
                if not node:
                    return group_tail
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            group_tail.next = rev(node, group_count + 1) # call with head of next group
            return prev

        return rev(head, 0)

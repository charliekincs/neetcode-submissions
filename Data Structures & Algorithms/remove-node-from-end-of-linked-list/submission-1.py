# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        if length == n:
            return head.next
        
        node_before_remove = length - n
        cur = head
        while node_before_remove > 1:
            cur = cur.next
            node_before_remove -= 1
        if cur.next.next:
            cur.next = cur.next.next
        else:
            cur.next = None

        return head
        

        

        
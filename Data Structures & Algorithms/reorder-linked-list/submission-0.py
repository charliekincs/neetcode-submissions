# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        
        nxt = slow.next
        slow.next = None
        mid = nxt

        prev = None
        cur = mid
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        cur = head
        while prev:
            cur_nxt = cur.next
            prev_nxt = prev.next
            cur.next = prev
            prev.next = cur_nxt
            cur = cur_nxt
            prev = prev_nxt


        
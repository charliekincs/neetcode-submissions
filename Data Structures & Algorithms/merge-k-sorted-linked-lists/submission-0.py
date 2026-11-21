# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or lists == [] or lists == [[]]:
            return None
        heap = []
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        
        if not heap:
            return None
        
        head = ListNode()
        node = head
        while heap:
            cur = heapq.heappop(heap)
            node.val = cur
            if heap:
                node.next = ListNode()
                node = node.next
        
        return head
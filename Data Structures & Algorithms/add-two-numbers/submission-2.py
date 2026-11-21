# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        carry = 0
        while l1 or l2 or carry:
            cur_sum = carry
            if l1:
                cur_sum += l1.val
            if l2:
                cur_sum += l2.val
            str_cur_sum = str(cur_sum)
            if len(str_cur_sum) == 2:
                carry = int(str_cur_sum[0])
                cur_sum = int(str_cur_sum[1])
            else:
                carry = 0

            cur.val = cur_sum
            if (l1 and l1.next) or (l2 and l2.next) or carry:
                cur.next = ListNode()
                cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return res

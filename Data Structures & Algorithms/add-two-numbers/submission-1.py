# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode(0, None)
        cur_node = res
        while l1 or l2:
            cur_sum = 0
            if l1:
                cur_sum += l1.val
                l1 = l1.next
            if l2:
                cur_sum += l2.val
                l2 = l2.next
            if carry != 0:
                cur_sum += carry

            if cur_sum > 9:
                str_cur_sum = str(cur_sum)
                cur_sum = int(str_cur_sum[-1])
                carry = int(str_cur_sum[0])
            else:
                carry = 0

            cur_node.val = cur_sum
            if l1 or l2:
                cur_node.next = ListNode(0, None)
                cur_node = cur_node.next

        if carry != 0:
            cur_node.next = ListNode(carry, None)
        return res
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        carry = 0
        while l1 or l2 or carry: 
            c1 = l1.val if l1 else 0
            c2 = l2.val if l2 else 0

            val = c1 + c2 + carry
            carry = val // 10
            val = val % 10 
            res.next = ListNode(val)

            res = res.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0

        return dummy.next
            
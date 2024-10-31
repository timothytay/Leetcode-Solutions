# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur1 = l1
        cur2 = l2
        dummy = ListNode
        curRes = dummy
        carry = 0
        while cur1 and cur2:
            res = cur1.val + cur2.val + carry
            carry = 0
            if res >= 10:
                res -= 10
                carry = 1
            curRes.next = ListNode(res)
            curRes = curRes.next
            cur1 = cur1.next
            cur2 = cur2.next

        while cur1:
            res = cur1.val + carry
            carry = 0
            if res >= 10:
                res -= 10
                carry = 1
            curRes.next = ListNode(res)
            curRes = curRes.next

            cur1 = cur1.next

        while cur2:
            res = cur2.val + carry
            carry = 0
            if res >= 10:
                res -= 10
                carry = 1
            curRes.next = ListNode(res)
            curRes = curRes.next

            cur2 = cur2.next

        if carry == 1:
            curRes.next = ListNode(carry)

        return dummy.next
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
        dummy = ListNode()
        cur = dummy
        cur1 = l1
        cur2 = l2
        carry = 0
        while cur1 or cur2 or carry != 0:
            cur1Val = cur1.val if cur1 else 0
            cur2Val = cur2.val if cur2 else 0
            res = cur1Val + cur2Val + carry
            carry = res // 10
            cur.next = ListNode(res % 10)
            cur = cur.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        return dummy.next
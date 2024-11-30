# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
         # 2 pointers, one at current of each node
         # add the values 
         # if the values add to more than 10, set the current value to sum - 10
         # carry variable
         # edge cases: trailing nodes for one list after other pointer goes out of bounds
         # another: carry after both nodes finish (add another node)
        
        dummy = ListNode(0)
        cur1 = l1
        cur2 = l2
        res = dummy
        carry = 0
        while cur1 and cur2:
            added = cur1.val + cur2.val + carry
            carry = 0
            if added >= 10:
                added -= 10
                carry = 1
            res.next = ListNode(added)
            cur1, cur2, res = cur1.next, cur2.next, res.next

        leftover = cur1 if cur1 else cur2
        while leftover or carry > 0:
            added = (leftover.val if leftover else 0) + carry
            carry = 0
            if added >= 10:
                added -= 10
                carry = 1
            res.next = ListNode(added)
            res = res.next
            leftover = leftover.next if leftover else None

        return dummy.next

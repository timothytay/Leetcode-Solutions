# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and not head.next:
            return None
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        dummy = ListNode()
        dummy.next = head
        dest = length - n 
        cur = dummy
        idx = 0
        while idx < dest:
            cur = cur.next
            idx += 1
        cur.next = cur.next.next
        return dummy.next

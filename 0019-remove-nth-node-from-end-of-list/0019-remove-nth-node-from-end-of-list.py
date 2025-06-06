# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        target = count - n

        if target == 0:
            return head.next

        cur = head
        for i in range(target - 1):
            cur = cur.next
        cur.next = cur.next.next

        return head
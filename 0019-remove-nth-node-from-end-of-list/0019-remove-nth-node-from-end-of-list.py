# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            fast = fast.next
        slow = head
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        if prev:
            prev.next = slow.next
        else:
            head = head.next
        return head
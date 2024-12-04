# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # algorithm structure
        # prev and cur pointers
        # store cur.next
        # point cur.next to prev
        # move prev to cur and cur to cur.next (stored)
        # when cur out of bounds, we have reached end, so return prev

        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev
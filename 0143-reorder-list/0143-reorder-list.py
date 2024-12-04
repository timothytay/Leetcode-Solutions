# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        prev = None
        slow.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        
        back = prev
        front = head
        dummy = ListNode()
        cur = dummy
        while front and back:
            cur.next = front
            front = front.next
            cur = cur.next
            cur.next = back
            back = back.next
            cur = cur.next
        if front:
            cur.next = front
        if back:
            cur.next = back
        return dummy.next
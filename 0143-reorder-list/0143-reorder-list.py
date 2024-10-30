# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, cur = slow, slow.next
        prev.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        end = prev
        start = head
        while start != end and start and end and start.next and end.next:
            tmp1 = start.next
            tmp2 = end.next
            start.next = end
            end.next = tmp1
            start = tmp1
            end = tmp2


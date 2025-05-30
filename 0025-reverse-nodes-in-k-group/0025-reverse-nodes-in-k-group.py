# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        
        count = 0
        cur = head
        while cur and count < k:
            count += 1
            cur = cur.next
        if count < k:
            return head
        end = cur

        prev, cur = None, head 
        while cur and cur != end:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        head.next = self.reverseKGroup(end, k)

        return prev

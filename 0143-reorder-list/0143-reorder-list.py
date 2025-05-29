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
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur1, cur2 = slow, slow.next
        slow.next = None
        while cur1 and cur2:
            tmp = cur2.next
            cur2.next = cur1
            cur1, cur2 = cur2, tmp

        cur1, cur2 = head, cur1
        
        while cur1 and cur2: # works for even because at the last step, cur1 moves to null and cur2 points to cur1 after
            tmp = cur1.next
            cur1.next = cur2
            cur1 = tmp
            tmp = cur2.next
            cur2.next = cur1
            cur2 = tmp
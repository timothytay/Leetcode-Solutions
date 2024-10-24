# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        prev = dummy
        node1 = list1
        node2 = list2
        while node1 and node2:
            if node1.val < node2.val:
                prev.next = node1
                node1 = node1.next
            else:
                prev.next = node2
                node2 = node2.next
            prev = prev.next
        if node1:
            prev.next = node1
        if node2:
            prev.next = node2
        return dummy.next
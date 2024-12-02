# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        curPos = 0
        while len(nodes) - curPos >= k:
            for i in range(curPos + k - 1, curPos, -1):
                nodes[i].next = nodes[i - 1]
            nodes[curPos].next = nodes[curPos + k] if curPos + k < len(nodes) else None
            if curPos - k >= 0:
                nodes[curPos - k].next = nodes[curPos + k - 1] 

            curPos += k 

        return nodes[k - 1]
            
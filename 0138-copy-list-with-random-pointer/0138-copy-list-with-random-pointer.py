"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # have one pass where you copy the nodes and their next pointers
        # on second pass copy random pointers 
        # store in a hash map where original node points to new node
        if not head:
            return None
        oldToNew = {}
        dummy = Node(0)
        currNew = dummy
        curr = head
        while curr:
            newNode = ListNode(curr.val)
            oldToNew[curr] = newNode
            currNew.next = newNode
            currNew = currNew.next
            curr = curr.next
            
        curr = head
        currNew = dummy.next

        while curr:
            currNew.random = oldToNew[curr.random] if curr.random else None
            currNew = currNew.next
            curr = curr.next

        return dummy.next

        


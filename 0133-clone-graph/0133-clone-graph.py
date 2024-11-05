"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        startNode = Node(node.val)
        nodes = {}
        nodes[node.val] = startNode
        def bfs(node):
            visit = set()
            visit.add(node)
            queue = deque()
            queue.append(node)
            while queue:
                for i in range(len(queue)):
                    curr = queue.popleft()
                    currCopy = nodes[curr.val]
                    for neighbor in curr.neighbors:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            queue.append(neighbor)
                            nodes[neighbor.val] = Node(neighbor.val)
                        currCopy.neighbors.append(nodes[neighbor.val])
        bfs(node)
        return startNode
        
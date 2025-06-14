"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        node_map = {}
        seen = set()

        def bfs(node):
            q = deque()
            q.appendleft(node)
            node_map[node] = Node(node.val)

            while len(q) > 0:
                for i in range(len(q)):
                    cur = q.pop()
                    if cur not in seen:
                        seen.add(cur)
                        for nei in cur.neighbors:
                            if nei not in node_map:
                                node_map[nei] = Node(nei.val)
                            node_map[cur].neighbors.append(node_map[nei])
                            if nei not in seen:
                                q.appendleft(nei)

        bfs(node)

        return node_map[node]
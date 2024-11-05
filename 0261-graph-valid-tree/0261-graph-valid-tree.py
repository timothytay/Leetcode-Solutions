from collections import deque
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
            
        def dfs(node, prev, visit):

            if node in visit:
                return False
            visit.add(node)
            for nei in adjList[node]:
                if nei != prev:
                    if not dfs(nei, node, visit):
                        return False
            return True

        visit = set()
        return dfs(0, float('inf'), visit) and len(visit) == n
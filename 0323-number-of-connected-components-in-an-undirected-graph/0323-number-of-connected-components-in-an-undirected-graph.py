class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = {key:[] for key in range(n)}
        for node1, node2 in edges:
            
            adj[node1].append(node2)
            adj[node2].append(node1)
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
            return
        count = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                count += 1
        return count
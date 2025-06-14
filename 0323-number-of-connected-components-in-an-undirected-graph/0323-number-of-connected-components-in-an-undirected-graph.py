class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(n)}
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node, seen):
            if node in seen:
                return 
            seen.add(node)
            for nei in adj_list[node]:
                dfs(nei, seen)

        count = 0
        seen = set()

        for node in adj_list.keys():
            if node not in seen:
                dfs(node, seen)
                count += 1

        return count
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a tree is a connected acyclic graph
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        def cycle(adj_list, node, path, prev, visit):
            if node in path:
                return True
            visit.add(node)
            path.add(node)
            for nei in adj_list[node]:
                if nei != prev:
                    if cycle(adj_list, nei, path, node, visit):
                        return True
            path.remove(node)
            return False

        visit = set()

        return not cycle(adj_list, 0, set(), -1, visit) and len(visit) == n
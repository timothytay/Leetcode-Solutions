class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        def bfs(start, adj, k):
            seen = set()
            q = deque()
            distTo = {}
            q.appendleft(start)
            distTo[start] = 0
            targetCount = 1
            while len(q) > 0:
                cur = q.pop()
                if distTo[cur] >= k or cur in seen:
                    continue
                seen.add(cur)
                for nei in adj[cur]:
                    if nei not in seen:
                        distTo[nei] = distTo[cur] + 1
                        q.appendleft(nei)
                        targetCount += 1
            return targetCount

        adj1 = defaultdict(list)
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
            
        adj2 = defaultdict(list)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        maxTargetsFrom2 = 0
        for i in range(len(edges2) + 1):
            maxTargetsFrom2 = max(bfs(i, adj2, k - 1), maxTargetsFrom2)

        ans = []

        for i in range(len(edges1) + 1):
            ans.append(bfs(i, adj1, k) + (maxTargetsFrom2 if k > 0 else 0))

        return ans
        

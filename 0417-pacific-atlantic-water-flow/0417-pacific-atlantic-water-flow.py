class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        aq = deque()
        pq = deque()
        aVisit = set()
        pVisit = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for row in range(rows):
            aq.append((row, cols-1))
            aVisit.add((row, cols-1))
            pq.append((row, 0))
            pVisit.add((row, 0))
        for col in range(cols):
            aq.append((rows-1, col))
            aVisit.add((rows-1, col))
            pq.append((0, col))
            pVisit.add((0, col))
        while aq:
            r, c = aq.popleft()
            prevHeight = heights[r][c]
            for dr, dc in directions:
                if min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or heights[r+dr][c+dc] < prevHeight or (r+dr, c+dc) in aVisit:
                    continue
                aq.append((r+dr, c+dc))
                aVisit.add((r+dr, c+dc))
        while pq:
            r, c = pq.popleft()
            prevHeight = heights[r][c]
            for dr, dc in directions:
                if min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or heights[r+dr][c+dc] < prevHeight or (r+dr, c+dc) in pVisit:
                    continue
                pq.append((r+dr, c+dc))
                pVisit.add((r+dr, c+dc))

        res = []
        for pos in pVisit:
            if pos in aVisit:
                res.append(list(pos))
        return res
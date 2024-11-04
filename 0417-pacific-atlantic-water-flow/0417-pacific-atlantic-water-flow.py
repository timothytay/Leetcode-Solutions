class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        canReach = []
        visit = set()
        def dfsPacific(heights, r, c, visit, prevHeight):
            rows = len(heights)
            cols = len(heights[0])
            if min(r, c) < 0:
                return True
            if r == rows or c == cols or heights[r][c] > prevHeight or (r, c) in visit:
                return False
            visit.add((r, c))
            hasPath = dfsPacific(heights, r+1, c, visit, heights[r][c]) or dfsPacific(heights, r-1, c, visit, heights[r][c]) or dfsPacific(heights, r, c+1, visit, heights[r][c]) or dfsPacific(heights, r, c-1, visit, heights[r][c])
            visit.remove((r, c))
            return hasPath

        def dfsAtlantic(heights, r, c, visit, prevHeight):
            rows = len(heights)
            cols = len(heights[0])
            if r == rows or c == cols:
                return True
            if min(r, c) < 0 or heights[r][c] > prevHeight or (r, c) in visit:
                return False
            visit.add((r, c))
            hasPath = dfsAtlantic(heights, r+1, c, visit, heights[r][c]) or dfsAtlantic(heights, r-1, c, visit, heights[r][c]) or dfsAtlantic(heights, r, c+1, visit, heights[r][c]) or dfsAtlantic(heights, r, c-1, visit, heights[r][c])
            visit.remove((r, c))
            return hasPath

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if dfsAtlantic(heights, row, col, visit, float('inf')) and dfsPacific(heights, row, col, visit, float('inf')):
                    canReach.append([row, col])
        return canReach
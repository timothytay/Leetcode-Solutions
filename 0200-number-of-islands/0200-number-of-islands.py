class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        islands = 0
        def dfs(grid, r, c, visited):
            rows = len(grid)
            columns = len(grid[0])
            if min(r, c) < 0 or r == rows or c == columns or grid[r][c] == '0' or (r, c) in visited:
                return
            visited.add((r, c))
            dfs(grid, r+1, c, visited)
            dfs(grid, r-1, c, visited)
            dfs(grid, r, c+1, visited)
            dfs(grid, r, c-1, visited)
            return 

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == '1':
                    islands += 1
                    dfs(grid, row, col, visited)
        return islands

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        def dfs(grid, r, c):
            rows = len(grid)
            columns = len(grid[0])
            if min(r, c) < 0 or r >= rows or c >= columns or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(grid, r+1, c)
            dfs(grid, r-1, c)
            dfs(grid, r, c+1)
            dfs(grid, r, c-1)
            return 

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(grid, row, col)
        return islands

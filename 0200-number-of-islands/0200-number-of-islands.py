class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        seen = set()
        def dfs(grid, row, col):
            if (row, col) in seen:
                return 
            ROWS, COLS = len(grid), len(grid[0])
            if min(row, col) < 0 or row >= ROWS or col >= COLS or grid[row][col] == '0':
                return 
            seen.add((row, col))
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)
            return 
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] == '1':
                    count += 1
                    dfs(grid, r, c)
        return count
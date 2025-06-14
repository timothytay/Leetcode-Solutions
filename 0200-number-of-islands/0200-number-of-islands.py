class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid, row, col):
            ROWS, COLS = len(grid) - 1, len(grid[0]) - 1
            if row < 0 or row > ROWS or col < 0 or col > COLS or grid[row][col] != '1':
                return
            grid[row][col] = '0'
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)

        number = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(grid, row, col)
                    number += 1
        return number 
        
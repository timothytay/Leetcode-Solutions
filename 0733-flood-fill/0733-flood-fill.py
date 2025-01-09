class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(grid, r, c, visit, initialColor, newColor):
            ROWS, COLS = len(grid), len(grid[0])
            if (r, c) in visit or r == ROWS or c == COLS or min(r, c) < 0 or grid[r][c] != initialColor:
                return
            grid[r][c] = newColor
            visit.add((r, c))
            dfs(grid, r+1, c, visit, initialColor, newColor)
            dfs(grid, r-1, c, visit, initialColor, newColor)
            dfs(grid, r, c+1, visit, initialColor, newColor)
            dfs(grid, r, c-1, visit, initialColor, newColor)
        visit = set()
        dfs(image, sr, sc, visit, image[sr][sc], color)

        return image
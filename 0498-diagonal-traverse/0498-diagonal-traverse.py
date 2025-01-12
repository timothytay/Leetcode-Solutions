class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = 0, 0 
        m, n = len(mat), len(mat[0])
        res = []
        while min(row, col) >= 0 and row < m and col < n:

            while row >= 0 and col < n:
                res.append(mat[row][col])
                row -= 1
                col += 1

            if col < n:
                row += 1
            else:
                row += 2
                col -= 1

            while row < m and col >= 0:
                res.append(mat[row][col])
                row += 1
                col -= 1

            if row < m:
                col += 1
            else:
                row -= 1
                col += 2

        return res




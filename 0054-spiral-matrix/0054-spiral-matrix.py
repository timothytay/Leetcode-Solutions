class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, n - 1
        up, down = 0, m - 1
        res = []
        while len(res) < m * n:
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1

            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1

            if up <= down:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1

            if right >= left:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

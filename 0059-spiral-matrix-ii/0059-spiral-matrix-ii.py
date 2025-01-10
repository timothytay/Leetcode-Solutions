class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        cur = 1
        left, right = 0, n - 1
        up, down = 0, n - 1
        
        while cur <= n * n:
            for i in range(left, right + 1):
                res[up][i] = cur
                cur += 1
            up += 1

            for i in range(up, down + 1):
                res[i][right] = cur
                cur += 1
            right -= 1

            if down >= up:
                for i in range(right, left - 1, -1):
                    res[down][i] = cur
                    cur += 1
                down -= 1

            if right >= left:
                for i in range(down, up - 1, -1):
                    res[i][left] = cur
                    cur += 1
                left += 1

        return res
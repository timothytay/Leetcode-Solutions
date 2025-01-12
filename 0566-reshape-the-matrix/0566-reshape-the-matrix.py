class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        reshaped = [[0] * c for _ in range(r)]
        
        curR, curC = 0, 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if curC == c:
                    curC = 0
                    curR += 1
                reshaped[curR][curC] = mat[i][j]
                curC += 1
        return reshaped

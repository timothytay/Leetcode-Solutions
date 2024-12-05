class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows + 1):
            if i <= 2:
                res.append([1] * i)
            else:
                curRow = [1]
                l, r = 0, 1
                while r < len(res[i-2]):
                    curRow.append(res[i-2][l] + res[i-2][r])
                    l += 1
                    r += 1
                curRow.append(1)
                res.append(curRow)
        return res
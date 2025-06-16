class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        
        elements_left = len(matrix) * len(matrix[0])

        top, right, bottom, left = 0, len(matrix[0]) - 1, len(matrix) - 1, 0

        while elements_left > 0:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
                elements_left -= 1
                if elements_left == 0:
                    return ans
            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
                elements_left -= 1
                if elements_left == 0:
                    return ans
            right -= 1

            
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
                elements_left -= 1
                if elements_left == 0:
                    return ans
            bottom -= 1

            
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
                elements_left -= 1
                if elements_left == 0:
                    return ans
            left += 1

        return ans
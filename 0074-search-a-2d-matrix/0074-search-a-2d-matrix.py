class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        length = m * n
        l = 0
        r = length-1
        
        while l <= r and l >= 0 and r < length:
            m = (l+r) // 2
            mi = m // n
            mj = m % n
            if target > matrix[mi][mj]:
                l = m + 1
            elif target < matrix[mi][mj]:
                r = m - 1
            else:
                return True
        return False
                 

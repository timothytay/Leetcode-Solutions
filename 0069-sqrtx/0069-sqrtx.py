class Solution:
    def mySqrt(self, x: int) -> int:
        closest = 0
        low, high = 1, x
        while low <= high:
            m = (low + high) // 2
            if m * m == x:
                return m
            if m * m > x:
                high = m - 1
            if m * m < x:
                closest = m
                low = m + 1
        return closest
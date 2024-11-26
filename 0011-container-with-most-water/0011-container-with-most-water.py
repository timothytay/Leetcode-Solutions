class Solution:
    def maxArea(self, height: List[int]) -> int:
        curMax = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            curMax = max(curMax, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return curMax
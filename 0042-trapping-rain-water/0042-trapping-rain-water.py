class Solution:
    def trap(self, height: List[int]) -> int:
        dpLeft = [0] * len(height)
        dpRight = [0] * len(height)
        total = 0
        for i in range(1, len(height)):
            dpLeft[i] = max(dpLeft[i-1], height[i-1])
        for i in range(len(height) - 2, -1, -1):
            dpRight[i] = max(dpRight[i+1], height[i+1])
        for i in range(len(height)):
            if min(dpLeft[i], dpRight[i]) > height[i]:
                total += min(dpLeft[i], dpRight[i]) - height[i]
        return total

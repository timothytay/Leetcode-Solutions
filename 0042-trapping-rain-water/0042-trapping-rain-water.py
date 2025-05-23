class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        i = 0
        leftMax, rightMax = height[0], height[-1]
        l, r = 0, len(height) - 1
        while l < r:
            if leftMax <= rightMax:
                l += 1
                if height[l] < leftMax:
                    total += leftMax - height[l]
                else:
                    leftMax = height[l]
            else:
                r -= 1
                if height[r] < rightMax:
                    total += rightMax - height[r]
                else:
                    rightMax = height[r]
        return total
                



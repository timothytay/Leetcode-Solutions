class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        while l < r:
            if maxLeft < maxRight:
                l += 1
                if maxLeft > height[l]:
                    total += (maxLeft - height[l])
                maxLeft = max(height[l], maxLeft)
            else:
                r -= 1
                if maxRight > height[r]:
                    total += (maxRight - height[r]) 
                maxRight = max(height[r], maxRight)
        return total

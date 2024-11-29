class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []  # Stack to store indices of the bars
        curMax = 0
        n = len(heights)
        
        for i in range(n):
            # While the current bar is less than the bar at the top of the stack
            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                # Calculate the width
                width = i if not stack else i - stack[-1] - 1
                # Calculate the area with heights[top] as the smallest bar
                curMax = max(curMax, heights[top] * width)
            stack.append(i)  # Push current index to stack
        
        # Process remaining bars in the stack
        while stack:
            top = stack.pop()
            width = n if not stack else n - stack[-1] - 1
            curMax = max(curMax, heights[top] * width)
        
        return curMax
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        right, left = [len(heights) - 1] * len(heights), [0] * len(heights)

        for i in range(len(heights)):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] > heights[i]:
                    right[stack[-1]] = i - 1
                    stack.pop()
                stack.append(i)

        stack = []
        for i in range(len(heights) - 1, -1, -1):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] > heights[i]:
                    left[stack[-1]] = i + 1
                    stack.pop()
                stack.append(i)

        largest = 0

        for i in range(len(heights)):
            largest = max(largest, heights[i] * (right[i] - left[i] + 1))

        return largest

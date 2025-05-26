class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        for i in range(len(nums) - k + 1):
            
            while heap and not (i <= heap[0][1] < i + k):
                heapq.heappop(heap)
            ans.append(-heap[0][0])
            if i + k < len(nums):
                heapq.heappush(heap, (-nums[i + k], i + k))


        return ans
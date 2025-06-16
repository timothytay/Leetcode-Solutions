class MedianFinder:

    def __init__(self):
        self.upper = [] # min-heap
        self.lower = [] # max-heap so negative numbers
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size += 1
        if not self.lower or num >= -1 * self.lower[0]:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -num)
        if len(self.upper) - len(self.lower) > 1:
            num_to_swap = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -1 * num_to_swap)
        elif len(self.lower) - len(self.upper) > 1:
            num_to_swap = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.upper, num_to_swap)

    def findMedian(self) -> float:
        if self.size % 2:
            if len(self.upper) > len(self.lower):
                return self.upper[0]
            else:
                return -1 * self.lower[0]
        else:
            return (self.upper[0] + -1 * self.lower[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
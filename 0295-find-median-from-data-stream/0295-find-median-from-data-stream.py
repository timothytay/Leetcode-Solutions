import heapq

class MedianFinder:

    def __init__(self):
        # max heap so push negative numbers
        self.lower = []
        # min heap so default usage with heapq
        self.upper = []
        heapq.heapify(self.lower)
        heapq.heapify(self.upper)
        self.count = 0

    def addNum(self, num: int) -> None:
        if not self.lower and not self.upper:
            heapq.heappush(self.lower, -num)
        else:
            if self.lower and -num < self.lower[0]:
                heapq.heappush(self.upper, num)
            else:
                heapq.heappush(self.lower, -num)
        self.count += 1
        while len(self.lower) - len(self.upper) > 1:
            tmp = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, tmp)
        while len(self.upper) - len(self.lower) > 1:
            tmp = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -tmp)

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (-self.lower[0] + self.upper[0]) / 2
        else:
            if len(self.upper) > len(self.lower):
                return self.upper[0]
            else:
                return -self.lower[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
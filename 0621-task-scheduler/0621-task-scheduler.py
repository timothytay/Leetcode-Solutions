class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        for t in tasks:
            freqs[t] = 1 + freqs.get(t, 0)
        
        heapLeft = [[-freq, task] for task, freq in freqs.items()]
        cannot = {}
        heapq.heapify(heapLeft)
        timestamp = 0

        while len(heapLeft) > 0 or len(cannot) > 0:
            timestamp += 1
            if timestamp in cannot:
                heapq.heappush(heapLeft, cannot[timestamp])
                cannot.pop(timestamp)
            if not heapLeft:
                continue
            cur = heapq.heappop(heapLeft)
            cur[0] += 1
            if cur[0] < 0:
                cannot[timestamp + n + 1] = cur

        return timestamp
            
            




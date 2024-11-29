from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.keys[key]
        l, r = 0, len(timestamps) - 1
        value = ""
        while l <= r:
            m = (l+r) // 2
            if timestamps[m][0] < timestamp:
                value = timestamps[m][1]
                l = m + 1
            elif timestamps[m][0] > timestamp:
                r = m - 1
            else:
                return timestamps[m][1]
        return value


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
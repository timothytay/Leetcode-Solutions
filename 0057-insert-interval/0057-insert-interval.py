class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # cases: new interval is in front, new interval is inbetween, new interval is after, new interval is before the end element of the last interval, new interval's end is after the next interval's start, intervals is empty 

        if not intervals:
            return [newInterval]

        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        
        i = 0
        ans = []

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        
        if i < len(intervals):
            modified_new_int = [min(intervals[i][0], newInterval[0]), newInterval[1]]

            while i < len(intervals) and intervals[i][0] <= newInterval[1]:
                i += 1

            modified_new_int[1] = max(modified_new_int[1], intervals[i-1][1])

            ans.append(modified_new_int)

            ans += intervals[i:]

        else:
            ans.append(newInterval)

        return ans

        
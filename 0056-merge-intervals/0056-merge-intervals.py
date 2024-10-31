class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1] and intervals[i][1] > res[-1][1]:
                res[-1][1] = intervals[i][1]
            elif intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
        return res

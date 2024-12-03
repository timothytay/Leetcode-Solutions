class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based on start 
        # for each interval which does not overlap with previous
        # keep a running largest end index to see if it continues to overlap
        # add then to a new result array
        # sorting them takes into account the possibility of next start being less than prev end but also less than prev start making them potentially not overlap 
        sortedInts = sorted(intervals, key=lambda x:x[0])
        res = []
        for start, end in sortedInts:
            if not res or res[-1][1] < start:
                res.append([start, end])
            elif end <= res[-1][1]:
                continue
            else:
                res[-1][1] = end
        return res


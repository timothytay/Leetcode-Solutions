class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        longestButton = events[0][0]
        timeTaken = events[0][1]
        for i in range(1, len(events)):
            time = events[i][1] - events[i-1][1]
            if time > timeTaken:
                longestButton = events[i][0]
                timeTaken = time
            if time == timeTaken and longestButton > events[i][0]:
                longestButton = events[i][0]
        return longestButton
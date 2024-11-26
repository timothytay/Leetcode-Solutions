class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        # s1 length is M and s2 length is N
        s1Map = {}
        for char in s1:
            s1Map[char] = s1Map.get(char, 0) + 1
        # {a:1, d:1, c:1}

        def isPermutation(s1Map, windowMap):
            for key, value in s1Map.items():
                if key not in windowMap or windowMap[key] != value:
                    return False
            return True

        for l in range(len(s2) - len(s1) + 1):
            windowMap = {}
            for char in s2[l:l+len(s1)]:
                windowMap[char] = windowMap.get(char, 0) + 1
            if isPermutation(s1Map, windowMap):
                return True
        return False
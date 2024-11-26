class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1, count2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        l = 0
        match = 0
        for i in range(26):
            if count1[i] == count2[i]:
                match += 1
        for r in range(len(s1), len(s2)):
            if match == 26:
                return True
            count2[ord(s2[l]) - ord('a')] -= 1
            if count2[ord(s2[l]) - ord('a')] == count1[ord(s2[l]) - ord('a')]:
                match += 1
            if count2[ord(s2[l]) - ord('a')] + 1 == count1[ord(s2[l]) - ord('a')]:
                match -= 1  
            l += 1
            count2[ord(s2[r]) - ord('a')] += 1
            if count2[ord(s2[r]) - ord('a')] == count1[ord(s2[r]) - ord('a')]:
                match += 1
            if count2[ord(s2[r]) - ord('a')] - 1 == count1[ord(s2[r]) - ord('a')]:
                match -= 1
            
        return match == 26
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        s1dict = {}
        for char in s1:
            s1dict[char] = 1 + s1dict.get(char, 0)
        l = 0
        window = {}
        have = 0
        for i in range(len(s1)):
            window[s2[i]] = 1 + window.get(s2[i], 0)
            if s2[i] in s1dict and window[s2[i]] == s1dict[s2[i]]:
                have += 1
        if have == len(s1dict.keys()):
            return True

        for r in range(len(s1), len(s2)):
            if s2[l] in s1dict and window[s2[l]] == s1dict[s2[l]]:
                have -= 1
            window[s2[l]] -= 1
            l += 1
            window[s2[r]] = 1 + window.get(s2[r], 0)
            if s2[r] in s1dict and window[s2[r]] == s1dict[s2[r]]:
                have += 1
            if have == len(s1dict.keys()):
                return True

        return False

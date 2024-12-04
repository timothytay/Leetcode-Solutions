class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
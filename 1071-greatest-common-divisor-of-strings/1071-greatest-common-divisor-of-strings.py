class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        endIndex = 0
        for r in range(min(len(str1), len(str2))):
            if self.isDivisor(str1[:r+1], str1) and self.isDivisor(str1[:r+1], str2):
                endIndex = r+1
            
        return str1[:endIndex] 

    def isDivisor(self, sub, full):
        test = ""
        while len(test) <= len(full):
            if test == full:
                return True
            test += sub
        return False
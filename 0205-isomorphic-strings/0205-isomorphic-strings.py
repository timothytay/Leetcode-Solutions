class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mappingS = {}
        mappingT = {}
        for i in range(len(s)):
            if s[i] in mappingS or t[i] in mappingT:
                if s[i] in mappingS and t[i] != mappingS[s[i]] or t[i] in mappingT and s[i] != mappingT[t[i]]:
                    return False
            else:
                mappingS[s[i]] = t[i]
                mappingT[t[i]] = s[i]
        return True
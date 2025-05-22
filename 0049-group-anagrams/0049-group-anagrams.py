from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for char in s:
                key[ord(char) - ord('a')] += 1
            groups[tuple(key)].append(s)
        return list(groups.values())

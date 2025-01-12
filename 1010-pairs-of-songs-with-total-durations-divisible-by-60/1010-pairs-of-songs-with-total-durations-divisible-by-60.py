class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mods = [dur % 60 for dur in time]
        seen = {}
        
        count = 0
        for mod in mods:
            if (60 - mod) % 60 in seen:
                count += seen[(60 - mod) % 60]
            seen[mod] = 1 + seen.get(mod, 0)
        return count 
            
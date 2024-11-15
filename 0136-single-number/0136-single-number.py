class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            
            if num in seen:
                seen[num] = True
            if num not in seen:
                seen[num] = False
        for num, boolean in seen.items():
            if not boolean:
                return num
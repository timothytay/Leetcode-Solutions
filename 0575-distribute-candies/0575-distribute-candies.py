class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = set()
        for candy in candyType:
            if candy not in types:
                types.add(candy)
        return len(types) if len(types) < len(candyType) / 2 else len(candyType) // 2
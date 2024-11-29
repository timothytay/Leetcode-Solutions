class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # some kind of binary search
        # testing different levels of k
        # finding the lowest one
        # we need to find a range
        # minimum would be 
        minSpeed = float('inf')
        lo, hi = 1, max(piles)
        while lo <= hi:
            mid = (lo+hi) // 2
            if self.isEnough(mid, piles, h):
                minSpeed = min(minSpeed, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return minSpeed

    def isEnough(self, speed, piles, h):
        for pile in piles:
            needed = pile // speed
            if pile % speed > 0:
                needed += 1
            if h < needed:
                return False
            h -= needed
        return True
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def fastEnough(speed, h):
            for pile in piles:
                h -= pile // speed
                if pile % speed:
                    h -= 1
            return h >= 0

        ans = max(piles)

        lo, hi = 1, max(piles)
        while lo <= hi:
            m = (lo + hi) // 2
            if fastEnough(m, h):
                ans = min(ans, m)
                hi = m - 1
            else:
                lo = m + 1
        
        return ans
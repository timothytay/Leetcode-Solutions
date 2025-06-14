class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        
        def climb(steps):
            if steps == n:
                return 1
            if steps > n:
                return 0
            if steps + 1 not in memo:
                memo[steps + 1] = climb(steps + 1)
            if steps + 2 not in memo:
                memo[steps + 2] = climb(steps + 2)
            return memo[steps + 1] + memo[steps + 2]

        return climb(0)


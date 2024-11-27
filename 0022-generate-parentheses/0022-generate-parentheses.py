class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bt(opening, closing, curOpening, cur):
            
            if opening > 0:
                cur += '('
                bt(opening - 1, closing, curOpening + 1, cur)
                cur = cur[:-1]
            if curOpening > 0:
                cur += ')'
                bt(opening, closing - 1, curOpening - 1, cur)
                cur = cur[:-1]
            if opening == 0 and closing == 0:
                res.append(cur)
        bt(n, n, 0, "")
        return res
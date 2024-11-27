class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur = ""
        s = []
        res = []
        def bt(opening, closing, cur, stack):
            if opening == 0 and closing == 0:
                res.append(cur)
             
                return
            if opening > 0:
                tempStack = stack
                stack.append('(')
                cur += '('
                bt(opening - 1, closing, cur, stack)
                cur = cur[:-1]
                stack = tempStack
            if stack and stack[-1] == '(':
                tempStack = stack
                cur += ')'
                stack.pop()
                bt(opening, closing - 1, cur, stack[:])
                cur = cur[:-1]
                stack = tempStack
            return
        bt(n, n, cur, s)
        return res
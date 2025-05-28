class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []

        def validParentheses(par):
            stack = []
            for char in par:
                if char == '(':
                    stack.append(char)
                elif char == ')':
                    if not stack:
                        return False
                    else:
                        stack.pop()
            return len(stack) == 0

        def generate(cur, opens, closes):
            if opens == 0 and closes == 0 and validParentheses(cur):
                ans.append(cur)
            else:
                if opens > 0:
                    generate(cur + '(', opens - 1, closes)
                if closes > 0:
                    generate(cur + ')', opens, closes - 1)

        generate("", n, n)

        return ans
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isnumeric() or (token[0] == '-' and token[1:].isnumeric()):
                stack.append(int(token))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if token == '+':
                    stack.append(val1+val2)
                elif token == '-':
                    stack.append(val1-val2)
                elif token == '/':
                    if val1 >= 0 and val2 >= 0 or val1 < 0 and val2 < 0:
                        stack.append(val1//val2)
                    else:
                        stack.append(-(abs(val1)//abs(val2)))
                elif token == '*':
                    stack.append(val1*val2)
        return stack[0]
class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')':'(', '}':'{', ']':'['}
        stack = []
        for p in s:
            if p not in matches:
                stack.append(p)
            if p in matches:
                if not stack or matches[p] != stack.pop():
                    return False
        return not stack
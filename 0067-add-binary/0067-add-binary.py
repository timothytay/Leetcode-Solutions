class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = False
        res = []
        while i >= 0 or j >= 0:
            result = '0'
            a_digit = a[i] if i >= 0 else '0'
            b_digit = b[j] if j >= 0 else '0'
            if a_digit == '1' and b_digit == '1':
                result = '0'
                if carry:
                    result = '1'
                carry = True
            elif a_digit == '1' or b_digit == '1':
                result = '1'
                if carry:
                    result = '0'
            else:
                result = '0'
                if carry:
                    result = '1'
                carry = False
            res.append(result)
            i -= 1
            j -= 1
        if carry:
            res.append('1')

        return ''.join(res[::-1])


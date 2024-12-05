class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverted = 0
        xCopy = x
        while xCopy > 0:
            digit = xCopy % 10
            reverted = reverted * 10 + digit
            xCopy //= 10

        return x == reverted 

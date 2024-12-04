class Solution:
    def isPalindrome(self, s: str) -> bool:
        # algorithm outline
        # 2 pointers, left and right
        # per iteration, compare left and right and if not same return false
        # if not alphanumeric, skip

        l, r = 0, len(s) - 1
        while l <= r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True
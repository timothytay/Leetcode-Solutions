class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1
                continue
            elif s[l].isalpha() and s[r].isalpha():
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                    continue
                else:
                    return False
            elif s[l].isnumeric() and s[r].isnumeric():
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                    continue
                else:
                    return False
            else:
                return False
        return True
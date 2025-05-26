class Solution:
    def reverseWords(self, s: str) -> str:
        sl = s.split(" ")
        l, r = 0, len(sl) - 1
        while l < r:
            if sl[l] == "":
                l += 1
            elif sl[r] == "":
                r -= 1
            else:
                sl[l], sl[r] = sl[r], sl[l]
                l += 1
                r -= 1
        ans = [word for word in sl if word != ""]
        return " ".join(ans)
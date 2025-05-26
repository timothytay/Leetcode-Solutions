class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        l, r = 0, len(s) - 1
        sList = list(s)
        while l < r:
            if sList[l].lower() not in vowels:
                l += 1
            elif sList[r].lower() not in vowels:
                r -= 1
            else:
                sList[l], sList[r] = sList[r], sList[l]
                l += 1 
                r -= 1
        return "".join(sList)
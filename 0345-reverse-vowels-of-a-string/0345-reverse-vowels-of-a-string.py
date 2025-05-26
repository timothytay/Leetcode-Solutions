class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        sVowels = []
        for char in s:
            if char.lower() in vowels:
                sVowels.append(char)
        i = len(sVowels) - 1
        newS = ""
        for char in s:
            if char.lower() in vowels:
                newS += sVowels[i]
                i -= 1
            else:
                newS += char
        return newS
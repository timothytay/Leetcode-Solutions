class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        total = 0
        counts = {}
        middle = False
        for word in words:
            counts[word] = 1 + counts.get(word, 0)
        for word in counts.keys():
            if word[::-1] in counts and word[0] != word[1]:
                add = min(counts[word], counts[word[::-1]])
                counts[word] -= add
                counts[word[::-1]] -= add
                total += add * 4
        for word, count in counts.items():
            if word[0] == word[1]:
                total += count // 2 * 4
                if count % 2 and not middle:
                    total += 2
                    middle = True
        return total
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars):
            ch = chars[i]
            j = i + 1
            while j < len(chars) and chars[j] == ch:
                j += 1
            for _ in range(j - i - 1):
                chars.pop(i + 1)
            count = j - i
            if count > 1:
                counts = [char for char in str(count)]
                for k in range(len(counts)):
                    chars.insert(i + k + 1, counts[k])
                i = i + len(counts) 
            i += 1
        return len(chars)
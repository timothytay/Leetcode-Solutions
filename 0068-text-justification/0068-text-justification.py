class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        words_left = len(words)
        lines = []
        i = 0
        while words_left > 0: # 7
            line = []
            word_count = 0
            words_cur_width = 0
            while i < len(words) and words_cur_width + word_count - 1 < maxWidth:
                if len(words[i]) <= maxWidth - words_cur_width - word_count - 1 + 1:
                    line.append(words[i])
                    words_cur_width += len(words[i])
                    words_left -= 1
                    word_count += 1
                    i += 1
                else:
                    break
            if i == len(words) or word_count == 1:
                final_line = ' '.join(line) 
                final_line += (maxWidth - len(final_line)) * ' '
            else:
                spaces = maxWidth - words_cur_width
                gap = spaces // (word_count - 1)
                leftover_spaces = spaces - gap * (word_count - 1)
                final_line = ""
                for j in range(len(line) - 1):
                    word = line[j]
                    final_line += word
                    final_line += ' ' * gap
                    if leftover_spaces > 0:
                        final_line += ' '
                        leftover_spaces -= 1
                final_line += line[-1]
                
            ans.append(final_line)
        return ans
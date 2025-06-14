class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        end = len(word)
        seen = set()
        def dfs(i, j, word_index):
            if word_index == end:
                return True
            elif i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or word_index >= end:
                return False
            elif (i, j) in seen:
                return False
            elif word[word_index] == board[i][j]:
                seen.add((i, j))
                right = dfs(i+1, j, word_index + 1)
                left = dfs(i-1, j, word_index + 1)
                up = dfs(i, j+1, word_index + 1)
                down = dfs(i, j-1, word_index + 1)
                seen.remove((i, j))

                return up or down or left or right

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False



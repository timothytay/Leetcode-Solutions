class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        def getStatus(r, c, board, ROWS, COLS):
            liveNeighbors = 0
            directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
            for dr, dc in directions:
                if min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS:
                    continue
                if board[r+dr][c+dc] == 1:
                    liveNeighbors += 1
            if board[r][c] == 1:
                if liveNeighbors < 2:
                    return 0
                elif 2 <= liveNeighbors <= 3:
                    return 1
                else:
                    return 0
            else:
                if liveNeighbors == 3:
                    return 1
                else:
                    return 0
                

        boardCopy = [row[:] for row in board]

        for row in range(len(board)):
            for col in range(len(board[0])):
                boardCopy[row][col] = getStatus(row, col, board, ROWS, COLS)

        for row in range(len(board)):
            for col in range(len(board[0])):
                board[row][col] = boardCopy[row][col]
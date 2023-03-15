def gameOfLife(self, board) -> None:
    #  1 -> 0  : 2
    #  1 -> 1  : 1
    #  1 -> 0  : 3
    #  0 -> 1  : 4

    row = len(board)
    col = len(board[0])

    def neicheck(ri, co):
        di = [[1, 0], [0, 1], [1, 1], [-1, 0], [0, -1], [- 1, - 1], [1, -1], [-1, 1]]

        count = 0
        for a in di:
            roo = ri + a[0]
            coo = co + a[1]

            if 0 <= roo < row and 0 <= coo < col and (
                    board[roo][coo] == 1 or board[roo][coo] == 2 or board[roo][coo] == 3):
                count = count + 1
        return count

    for r in range(row):
        for c in range(col):
            val = neicheck(r, c)
            if board[r][c] == 0:
                if val == 3:
                    board[r][c] = 4
            elif board[r][c] == 1:
                if val in [2, 3]:
                    board[r][c] = 1
                elif val > 3:
                    board[r][c] = 3
                elif val < 2:
                    board[r][c] = 2

    for i in board:
        print(i)

    for r in range(row):
        for c in range(col):
            if board[r][c] == 2:
                board[r][c] = 0
            elif board[r][c] == 3:
                board[r][c] = 0
            elif board[r][c] == 4:
                board[r][c] = 1
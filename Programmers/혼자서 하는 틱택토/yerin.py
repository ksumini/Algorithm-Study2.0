def check_bingo(board, mark):
    for i in range(3):
        if board[i] == (mark + mark + mark):
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True

    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    return False


def solution(board):
    o_cnt = sum(row.count("O") for row in board)
    x_cnt = sum(row.count("X") for row in board)

    o_bingo = check_bingo(board, "O")
    x_bingo = check_bingo(board, "X")

    if (o_cnt == x_cnt and not o_bingo) or (o_cnt == x_cnt + 1 and not x_bingo):
        return 1

    return 0
def win(board, A):
    """
    check if A win

    Params
        double_list board : 3*3 board
        char A : 'O' or 'X'

    Returns
        bool : result
    """
    for i in range(3):
        # row [i, 012]
        if A == board[i][0] == board[i][1] == board[i][2]:
            return True

        # col [012, i]
        if A == board[0][i] == board[1][i] == board[2][i]:
            return True

    # diag left -> right
    if A == board[0][0] == board[1][1] == board[2][2]:
        return True
    # diag right -> left
    if A == board[2][0] == board[1][1] == board[0][2]:
        return True
    return False


def solution(board):
    """
    check if A win

    Params
        double_list board : 3*3 board

    Returns
        int result : if board is possible outcome, return 1
    """
    count_O, count_X = 0, 0  # count 'O' and 'X'
    for i in range(3):
        count_O += board[i].count('O')
        count_X += board[i].count('X')

    # in case, 'X' is more numerous than 'O'
    if count_O < count_X:
        return 0

    # # in case, 'O' is more numerous than 'X'
    if count_O >= count_X + 2:
        return 0

    # In case of ‘O win’ and further progress
    if win(board, 'O') and (count_O != count_X + 1):
        return 0

    # In case of ‘X win’ and further progress
    if win(board, 'X') and (count_O != count_X):
        return 0

    return 1
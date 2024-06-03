def check_hit(board, r, c):
    hori = all([board[r][k] == board[r][c] for k in range(3)])  # 좌우
    if r == 0:
        vert = all([board[k][c] == board[r][c] for k in range(3)]) # 상하
        if c == 0:
            dig = all([board[k][k] == board[r][c] for k in range(3)]) # 대각선
            return hori or vert or dig
        elif c == 1:
            return vert
        elif c == 2:
            dig = all(board[k][2-k] == board[r][c] for k in range(3)) # 대각선
            return vert or dig
    else:
        return hori


def solution(board):
    win_mark = None
    is_hit = False  
    nums = [0, 0, 0]  # num_o, num_x, num_.
    mark = {
        'O': 0,
        'X': 1,
        '.': 2
    }
        
    for r in range(3):
        for c in range(3):
            nums[mark[board[r][c]]] += 1
            if board[r][c] != '.' and (r==0 or c==0):
                tmp_hit = check_hit(board, r, c)
                if is_hit and tmp_hit and win_mark != board[r][c]:
                    return 0
                if tmp_hit and win_mark is None:
                    win_mark = board[r][c]
                
                is_hit = is_hit if is_hit else tmp_hit
                                    
    if not is_hit and 0 <= nums[0] - nums[1] < 2:
        return 1
    else:
        if win_mark == 'O':
            if nums[0] - nums[1] == 1:
                return 1
        else:
            if nums[0] == nums[1]:
                return 1
    
    return 0

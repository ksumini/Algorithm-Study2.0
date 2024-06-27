def check_hit(board, r, c):
    hori = all([board[r][k] == board[r][c] for k in range(3)])  # 좌우
    if r == 0:
        vert = all([board[k][c] == board[r][c] for k in range(3)]) # 상하
        if c == 0:
            dig = all([board[k][k] == board[r][c] for k in range(3)]) # 대각선
            return hori or vert or dig  # [0,0] 가로, 세로, 대각선 빙고 확인
        elif c == 1:
            return vert # [0,1] 세로 빙고 확인
        elif c == 2:
            dig = all(board[k][2-k] == board[r][c] for k in range(3)) # 대각선
            return vert or dig # [0,2] 세로, 대각선 빙고 확인
    else:
        return hori # [1,0] [2,0] 가로 빙고 확인


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
                # 제일 윗줄: 가로, 세로, 대각선 빙고 확인 ([0,0] -> 가로 세로 대각선, [0,1] -> 세로, [0,2] -> 대각선, 세로)
                # 2, 3번째 줄: 가로 빙고 확인 ([1,0] -> 가로, [2.0] -> 가로)
                
                tmp_hit = check_hit(board, r, c) # 현재 row, column에서 빙고 확인
                if is_hit and tmp_hit and win_mark != board[r][c]: 
                    # 이전에 빙고가 있고 (is_hit), 현재도 빙고가 있는데(tmp_hit), 빙고 마크가 다른 경우 False
                    # 한번 놓을 때 빙고가 2번 되는 경우를 생각하는 데 오래 걸림
                    return 0
                if tmp_hit and win_mark is None:
                    # 현재 빙고 일 때, win_mark update
                    # win_mark is None 없어도 됨.
                    win_mark = board[r][c]

                # 이전에 빙고 확인(is_hit True)이 되었다면, is_hit은 계속 True 유지
                # 만약 이전에 빙고가 확인이 안 되었다면, 현재 빙고 상태로 is_hit update
                is_hit = is_hit if is_hit else tmp_hit
                                    
    if not is_hit and 0 <= nums[0] - nums[1] < 2:
        # 빙고가 없다면, O의 개수가 X보다 1개 많거나 같다.
        return 1
    else:
        if win_mark == 'O':
            if nums[0] - nums[1] == 1:
                # O 빙고라면 O의 개수가 1개 더 많음.
                return 1
        else:
            if nums[0] == nums[1]:
                # X 빙고라면 O와 X의 개수가 같음.
                return 1
    
    return 0

# 4번 이상 돌릴 필요 없음, 순서 정해져 있지 않음.
# 제일 위에 행 돌리면 나머지는 고정됨. -> 힌트 참고
# 복잡도 -> O(4^8 * 8^2) = 2^24 \approx 16,000,000

def product(arr: list, repeat: int=1) -> list:
    # 중복 순열
    result = [[]]
    pools = [arr] * repeat
    
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    
    return result
            

def rotate_sub_board(board: list, row:int, col: int, cnt: int):
    """
    board: 현재 시계 방향
    row: 회전 시킬 center의 row
    col: 회전 시킬 center의 col
    cnt: 회전 횟수
    """
    mvs = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    # 본인, 상, 하, 좌, 우
    for dr, dc in mvs:
        cur_r, cur_c = row + dr, col + dc
        if 0 <= cur_r < len(board) and 0 <= cur_c < len(board):
            board[cur_r][cur_c] += cnt
            board[cur_r][cur_c] %= 4
    

def rotate_board(board: list, rotate: list, cur_answer: int):
    """
    board: 현재 시계 방향
    rotate: 회전 시킬 조합
    cur_answer: 이전 조합들 중 회전이 가장 작은 횟수
    """
    result = 0
    # rotate first row
    for col, cnt in enumerate(rotate):
        if cnt > 0 :
            rotate_sub_board(board, 0, col, cnt)
            result += cnt
            
            # pruning
            if result > cur_answer:
                return cur_answer
    
    # rotate reamining row
    for row in range(1, len(board)):
        for col in range(len(board)):
            cnt = (4 - board[row-1][col]) % 4
            if cnt > 0:
                rotate_sub_board(board, row, col, cnt)
                result += cnt
                
                if result > cur_answer:
                    return cur_answer
    
    for col in range(len(board)):
        if board[len(board)-1][col] != 0:
            # 첫 번재 행을 돌린 경우의 수에 대해 불가능한 경우
            return cur_answer
    
    return result


def solution(clockHands):
    candidates = product(range(4), len(clockHands)) # 첫 번째 행 0 ~ 3번 돌리는 중복 순열
    answer = 4 * 64
    for candidate in candidates:
        answer = rotate_board([clockHand[:] for clockHand in clockHands], 
                              candidate, answer)
        
    return answer

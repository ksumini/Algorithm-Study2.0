def cal_mvs(finger: int, target: int) -> int:
    # 손가락과 목표 숫자의 좌표를 가져옴.
    src = row_col_of_number[finger]
    dest = row_col_of_number[target]    
    
    if src == dest:
        return 1
    
    diff_row = abs(src[0] - dest[0])
    diff_col = abs(src[1] - dest[1])
    
    mvs = 0
    
    # 대각선으로 움직임    
    mv_diagonal = min(diff_col, diff_row)
    mvs += (3 * mv_diagonal)
    
    diff_col -= mv_diagonal
    diff_row -= mv_diagonal
    
    # 좌우로 움직임
    if diff_row:
        mvs += (2 * diff_row)
        diff_row = 0
    
    # 상하로 움직임
    if diff_col:
        mvs += (2 * diff_col)
        diff_col = 0
    
    return mvs


def solution(numbers):
    global row_col_of_number
    # 각 숫자에 해당하는 좌표를 미리 정의해준다.
    # 이후 숫자 사이의 시간을 계산할 때 활용.
    row_col_of_number = {0: [3, 1]}
    for i in range(9):
        row_col_of_number[i+1] = [i // 3, i % 3]
        
    # 초기 dp의 값은 매우 큰 값을 준다.
    # 그리고 왼/오 손가락이 이동했을 때 값이 더 작은 것을 dp에 저장한다.
    # 왼손 또는 오른손을 현재 위치에서 다음 num 위치로 이동시켜야 한다.
    # 이때 현재 위치는 0 ~ 9이고, 왼손 오른손 모두를 생각하면 총 100가지의 경우의 수가 있다.
    # 그리고 왼손을 target 또는 오른손을 target에 이동시키는 2가지 이동이 존재하게 된다.
    dp = [[[float('inf')] * 10 for _ in range(10)] for _ in range(len(numbers) + 1)]
    dp[0][4][6] = 0  # 초기에 4, 6에 손가락이 있음
        
    for idx, num in enumerate(numbers):
        num = int(num)
        for left in range(10): 
            for right in range(10):
                if dp[idx][left][right] != float('inf') and left != right:
                    # 현재 위치가 될 수 있는 좌표와 왼손 오른손이 같은 좌표가 아닐 때
                    
                    mv_left = dp[idx][left][right] + cal_mvs(left, num)  # 왼손을 옮겼을 경우의 시간
                    mv_right = dp[idx][left][right] + cal_mvs(right, num) # 오른손을 옮겼을 경우의 시간
                                        
                    dp[idx+1][num][right] = min(dp[idx+1][num][right], mv_left) # 왼손을 옮겼다는 가정하에 update
                    dp[idx+1][left][num] = min(dp[idx+1][left][num], mv_right) # 오른손을 옮겼다는 가정하에 update
    
    return min(min(dp[-1], key=min))  # 2차원 배열에서 최소값을 가져옴.

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dm = [[0, 0], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1]] # → ↗ ↑ ↖ ← ↙ ↓ ↘

# 보드 확인 함수
def print_board():
    for b in board:
        print(*b)
    print()

# 초기의 영양제 위치
def get_medicine():
    return [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]

# 영양제 보드 반대편으로 이동
def set_out(i):
    if i < 0:
        return n + i
    elif i >= n:
        return i - n
    return i

# 영양제 특수 이동 규칙
def move_medicine(special_medicine, move):
    next_move = []
    d, p = move
    for x, y in special_medicine:
        nx = x + dm[d][0] * p
        ny = y + dm[d][1] * p
        nx = set_out(nx)
        ny = set_out(ny)
        next_move.append([nx, ny])
    return next_move

# 최종 높이 합 출력
def get_height():
    height = 0
    for b in board:
        height += sum(b)
    print(height)

sm = get_medicine()

for k in range(m):
    # 특수 영양제를 이동 규칙에 따라 이동
    sm = move_medicine(sm, map(int, input().split()))

    # 특수 영양제로 높이 1 성장
    for x, y in sm:
        board[x][y] += 1
        
    # 특수 영양제를 투입한 리브로수의 대각선으로 인접한 방향에 높이가 1 이상인 리브로수가 있는 만큼 높이가 더 성장
    for x, y in sm:
        for dx, dy in [[-1, -1], [1, -1], [-1, 1], [1, 1]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and board[nx][ny] >= 1:
                board[x][y] += 1

    # 특수 영양제를 투입한 리브로수를 제외하고 높이가 2 이상인 리브로수는 높이 2를 베어서 잘라낸 리브로수로 특수 영양제를 사고, 해당 위치에 다음 특수 영양제
    nsm = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and [i, j] not in sm:
                board[i][j] -= 2
                nsm.append([i, j])
    
    sm = nsm

get_height()
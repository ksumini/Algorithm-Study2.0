# 최적의 풀이 참고 - 168ms
import sys
input = sys.stdin.readline

dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

max_num = max(max(row) for row in board)    # 1칸의 최대 값

max_point = 0   # 정답

def dfs(x, y, i, total):    # i: 누적 칸, total: 누적 점수
    global max_point
    if (4-i) * max_num + total < max_point: # 해당 경우에서 나올 max 점수 < 최대 점수
        return 
    if i == 4:  # 4칸
        max_point = max(max_point, total)
        return 
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0<=nx<n and 0<=ny<m and board[nx][ny]:
            tmp = board[nx][ny]
            board[nx][ny] = 0
            if i == 2:  # T case
                dfs(x, y, i+1, total + tmp)
            dfs(nx, ny, i+1, total + tmp)
            board[nx][ny] = tmp

for i in range(n):
    for j in range(m):
        point = board[i][j]
        board[i][j] = 0
        dfs(i, j, 1, point)
        board[i][j] = point

print(max_point)

# 첫 풀이 - 3012ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

mimo = {
    'Z' : [
        [(0,0), (1,0), (1,1), (2,1)],
        [(0,0), (1,0), (1,-1), (2,-1)],
        [(0,0), (0,1), (1,1), (1,2)],
        [(0,0), (0,1), (-1,1), (-1,2)]
    ],
    'L' : [
        [(0,0), (1,0), (2,1), (2,0)],
        [(0,0), (1,0), (2,-1), (2,0)],
        [(0,0), (1,2), (0,1), (0,2)],
        [(0,0), (-1,2), (0,1), (0,2)],
        [(0,0), (-1,0), (-2,1), (-2,0)],
        [(0,0), (-1,0), (-2,-1), (-2,0)],
        [(0,0), (1,-2), (0,-1), (0,-2)],
        [(0,0), (-1,-2), (0,-1), (0,-2)]
    ],
    'T' : [
        [(0, 0), (1, 0), (0, -1), (0, 1)],
        [(-1, 0), (0, 0), (0, -1), (0, 1)],
        [(-1, 0), (1, 0), (0, 0), (0, 1)],
        [(-1, 0), (1, 0), (0, -1), (0, 0)]
    ],
    'I' : [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (0, 1), (0, 2), (0, 3)]
    ],
    'O' : [
        [(0, 0), (1, 0), (1, 1), (0, 1)]
    ]
}

def get_point(x, y, dxy):
    point = 0
    for dx, dy in dxy:
        if 0<=x+dx<n and 0<=y+dy<m:
            point += board[x+dx][y+dy]
        else:
            return 0
    return point

def mino(x, y):
    max_point = 0
    for shape in ['L', 'T', 'Z', 'I', 'O']:
        for dxy in mimo[shape]:
            max_point = max(max_point, get_point(x, y, dxy))
    
    return max_point

answer = 0

for i in range(n):
    for j in range(m):
        answer = max(answer, mino(i, j))

print(answer)
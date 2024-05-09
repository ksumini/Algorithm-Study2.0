from collections import deque


def solution(board):
    # 상,하,좌,우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n = len(board)
    m = len(board[0])

    INF = float('inf')
    dist = [[INF] * m for _ in range(n)]

    q = deque()
    # 시작지점
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append((i, j, 0))
                dist[i][j] = 0

    while q:
        x, y, cnt = q.popleft()

        # 목표지점에 도달한 경우
        if board[x][y] == 'G':
            return cnt

        # 상하좌우 이동
        for k in range(4):
            nx, ny = x, y

            while 0 <= nx + dx[k] < n and 0 <= ny + dy[k] < m and board[nx+dx[k]][ny+dy[k]] != 'D':
                nx += dx[k]
                ny += dy[k]

            if dist[nx][ny] > cnt + 1:
                dist[nx][ny] = cnt + 1
                q.append((nx, ny, cnt + 1))

    return -1


print(solution(board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))

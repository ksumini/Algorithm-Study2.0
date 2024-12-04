'''
직사각형 지도
힘 min, 높이 min

위로 가지 않고, 내려만 가는 코스 개수

'''
import sys
sys.setrecursionlimit(10**6)


m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dp[m-1][n-1] = 1


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and board[x][y] > board[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


print(dfs(0, 0))

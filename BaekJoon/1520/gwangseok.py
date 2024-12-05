import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(row, col):
    if DP[row][col] >= 0:
        return DP[row][col]

    DP[row][col] = 0

    mvs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for dr, dc in mvs:
        next_row, next_col = row + dr, col + dc
        if 0 <= next_row < M and 0 <= next_col < N and board[row][col] > board[next_row][next_col]:
            DP[row][col] += dfs(next_row, next_col)

    return DP[row][col]


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
DP = [[-1] * N for _ in range(M)]

start_row, start_col = 0, 0
end_row, end_col = M-1, N-1

DP[end_row][end_col] = 1
print(dfs(start_row, start_col))

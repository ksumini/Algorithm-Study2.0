from collections import deque
import heapq
import sys

input = sys.stdin.readline

n,m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

q = []

heapq.heappush(q,(-board[0][0], 0, 0)) # (높이 값, row, col)

dp[0][0] = 1

while q:    # 높이가 높은 칸 순서대로 탐색
    _, r, c = heapq.heappop(q) # (높이 값, row, col)
    if (r, c) == (n-1, m-1):
        continue
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < m and board[r][c] > board[nr][nc]:
            if dp[nr][nc] == 0: # q에 있는지 확인
                heapq.heappush(q,(-board[nr][nc], nr,nc))
            dp[nr][nc] += dp[r][c]

print(dp[n-1][m-1])
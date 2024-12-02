"""
<문제>
각 칸에는 높이가 쓰여있다.
각 지점 사이의 이동은 상하좌우 이웃한 곳끼리만 가능하다.
제일 왼쪽 위 칸에서 시작해 제일 오른쪽 아래 칸으로 이동하려고 한다.

항상 내리막길로만 이동하는 경로의 개수를 구하시오.

<풀이>
풀이 시간: 40분
1. dp[x][y]: (x, y)에서 도착점까지 갈 수 있는 경로의 개수
2. dfs 탐색
- 현재 위치에서 높이가 더 낮은 위치로 이동
- 이동 가능한 모든 경로의 개수를 dp[x][y]에 업데이트
3. Base condition
- 도착점에서는 경로의 개수 1


<시간 복잡도>
O(m * n): 격자의 모든 칸을 한번씩만 방문하기 때문에 중복 계산 방지
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 세로, 가로
m, n = map(int, input().split())
# 각 지점의 높이
height = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)] # dp[x][y]: (x, y) 지점에서 (m-1, n-1)까지 도달할 수 있는 경로의 개수
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 인접한 상하좌우


def dfs(x: int, y: int) -> int:
    # Base Condition
    if x == m - 1 and y == n - 1:
        return 1
    # 이미 계산된 경우, 중복 방지
    if dp[x][y] != -1:
        return dp[x][y]
    # 경로 초기화
    dp[x][y] = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and height[nx][ny] < height[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


print(dfs(0, 0))
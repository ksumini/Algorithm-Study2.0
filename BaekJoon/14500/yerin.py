def dfs(x, y, depth, total):
    global ans
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    if depth == 4:  # 최대값 갱신
        ans = max(ans, total)
        return None

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if depth == 2:  # 'ㅗ' 처리.
                visited[nx][ny] = True
                dfs(x, y, depth + 1, total + board[nx][ny])
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

print(ans)

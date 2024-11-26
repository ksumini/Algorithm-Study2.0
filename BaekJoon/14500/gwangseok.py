def dfs(cur_row, cur_col, cnt, max_v, cur_v):
    global N, M, board, visited

    if cnt == 4:
        return max(max_v, cur_v)

    # up, down, right, left
    mvs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    for dr, dc in mvs:
        next_r, next_c = cur_row + dr, cur_col + dc
        if 0 <= next_r < N and 0 <= next_c < M and not visited[next_r][next_c]:
            visited[next_r][next_c] = True
            if cnt == 2:
                # ㅏ, ㅓ, ...
                max_v = dfs(cur_row, cur_col, cnt + 1, max_v, cur_v + board[next_r][next_c])
            max_v = dfs(next_r, next_c, cnt + 1, max_v, cur_v + board[next_r][next_c])
            visited[next_r][next_c] = False
    
    return max_v


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

ans = 0
for row in range(N):
    for col in range(M):
        visited[row][col] = True
        ans = max(ans, dfs(row, col, 1, 0, board[row][col]))
        visited[row][col] = False

print(ans)

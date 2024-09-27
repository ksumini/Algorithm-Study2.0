from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def find_linked(maps, visited, loc):
    global dy, dx

    h = len(maps);
    w = len(maps[0])  # 맵 가로, 세로
    result = 0  # 연결된 땅 넓이

    q = deque()
    q.append(loc)

    y, x = loc  # 초기 위치 방문한거로 설정
    result += int(maps[y][x])
    visited[y][x] = 1  # check visited

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= h or nx >= w:  # out of maps
                continue

            if maps[ny][nx] == 'X':  # 바다임
                continue

            if visited[ny][nx] == 0:  # 연결되어있고, 아직 방문하지 않은 곳 추가
                q.append([ny, nx])
                visited[ny][nx] = 1  # 방문한거로 처리
                result += int(maps[ny][nx])
    return visited, result


def solution(maps):
    results = []

    h = len(maps);
    w = len(maps[0])
    visited = [[0] * w for _ in range(h)]  # 방문했는지 유무 처리

    for i in range(h):
        for j in range(w):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                visited, result = find_linked(maps, visited, [i, j])
                results.append(result)

    if results == []:  # 지낼 곳이 없음
        return [-1]

    results.sort()

    return results
'''
[2024-06-12] heewon #90

## 접근 방식
- 출발 -> 레버 -> 도착 이므로 레버에서 출발, 도착 까지의 거리의 합을 구한다.
- BFS로 구현

## 사용한 모듈
`deque`

## 추가 정보
- 시간: 1 hour 이하
- 힌트: `None`
'''

from collections import deque

def solution(maps:list):
    """
    지도 `maps`를 이용하여 출발지(S)에서 도착지(E)까지의 최단 거리를 반환하는 함수입니다.

    Args:
        maps: 2차원 리스트로 이루어진 지도 정보입니다.
              'X': 벽
              'L': 레버를 나타냅니다.
              'S': 시작점을 나타냅니다.
              'E': 도착점을 나타냅니다.

    Returns:
        출발지(S)에서 레버(L)을 지나고 도착지(E)까지의 최단 거리, 길을 찾을 수 없는 경우 -1을 반환합니다.
    """

    answer = 0

    # 상, 하, 좌, 우 이동 방향
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    # 출발지, 도착지 좌표 찾기
    lx, ly = 0, 0
    sx, sy = 0, 0
    ex, ey = 0, 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'L':
                lx, ly = i, j  # 출발지 위치 저장
            elif maps[i][j] == 'S':
                sx, sy = i, j  # 시작점 위치 저장
            elif maps[i][j] == 'E':
                ex, ey = i, j  # 도착점 위치 저장

    # 거리 정보를 저장할 2차원 리스트 (float('INF')은 매우 큰 값으로 초기화)
    distance = [[float('INF') for _ in range(len(maps[0]))] for _ in range(len(maps))]
    distance[lx][ly] = 0

    q = deque()
    q.append([lx, ly])

    while q:
        x, y = q.popleft()  # 큐에서 꺼내 현재 위치 확인

        # 상, 하, 좌, 우 탐색
        for i in range(4):
            xx = x + dx[i]  # 다음 위치 계산 (x 좌표)
            yy = y + dy[i]  # 다음 위치 계산 (y 좌표)

            # 지도 범위 내에 있고, 통로가 있는 경우만 이동
            if 0 <= xx < len(maps) and 0 <= yy < len(maps[0]) and maps[xx][yy] != 'X':
                # 현재 위치에서 다음 위치까지의 거리가 더 짧은 경우 갱신
                if distance[x][y] + 1 < distance[xx][yy]:
                    distance[xx][yy] = distance[x][y] + 1
                    q.append([xx, yy])  # 다음 위치를 큐에 추가

    # 시작점과 도착점까지의 거리가 모두 무한대(float('INF'))인 경우는 길을 찾을 수 없음
    if distance[sx][sy] == float('INF') or distance[ex][ey] == float('INF'):
        return -1

    # 최단 거리 계산 (출발지에서 레버까지 + 레버에서 도착점까지)
    answer += distance[sx][sy] + distance[ex][ey]
    return answer
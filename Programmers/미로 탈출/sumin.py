"""
<문제>
각 칸은 '통로' or '벽'('벽'으로는 지나갈 수 없고, '통로'로만 이동 가능)
- '문': 미로를 빠져나가는 문
- '레버': '통로'들 중 한 칸

1. 출발점에서 '레버'가 있는 칸으로 이동
2. '문'이 있는 칸으로 이동
- 레버를 당기지 않았더라도 출구가 있는 칸을 지나갈 수 있다.

<제한 사항>
- 5 ≤ maps의 길이 ≤ 100
    - 5 ≤ maps[i]의 길이 ≤ 100
- maps[i]는 다음 5개의 문자들로만 이루어져 있다.
    - S : 시작 지점
    - E : 출구
    - L : 레버
    - O : 통로
    - X : 벽
- 시작 지점과 출구, 레버는 항상 다른 곳에 존재하며 한 개씩만 존재한다.
- 출구는 레버가 당겨지지 않아도 지나갈 수 있으며, 모든 통로, 출구, 레버, 시작점은 여러 번 지나갈 수 있다.

<풀이 시간>
20분

<풀이>
1. 시작 지점에서 레버가 있는 곳까지 최단 거리 구하기
2. 레버에서 출구까지의 최단 거리 구하기

<시간복잡도>
O(NxM)
- BFS 함수: O(NxM)를 두 번 호출
    - BFS의 시간 복잡도는 O(V+E)
    - 여기서 V는 노드의 수, E는 간선의 수
    - 이 경우 V=N×M이고, E는 최악의 경우 4×(N×M)이므로, 시간 복잡도는 O(N×M)
- 시작 지점, 미로, 도착 지점을 찾기 위한 순회: O(NxM)
-> O(NxM) + O(NxM) + O(NxM) = O(NxM)
"""
from collections import deque


def bfs(maps: list, start: tuple, goal: tuple) -> int:
    """
    :param maps: 미로 배열
    :param start: 시작 지점
    :param goal: 도착 지점
    :return: 시작 지점에서 도착 지점까지 걸리는 최소 시간
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 큐에 시작 지점 삽입
    q = deque([start])
    # 방문처리 및 각 지점까지의 거리를 위한 딕셔너리
    distance = {start: 0}

    while q:
        # 현재칸 확인
        cur = q.popleft()
        # 도착지점에 도달하면 거리 반환
        if cur == goal:
            return distance[cur]

        for dx, dy in directions:
            nx, ny = cur[0] + dx, cur[1] + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X':
                if (nx, ny) not in distance:
                    q.append((nx, ny))
                    distance[(nx, ny)] = distance[cur] + 1

    # 도착점에 도달할 수 없는 경우 -1 반환
    return -1


def solution(maps: list) -> int:
    """
    :param maps: 미로를 나타낸 문자열 배열
    :return: 미로를 탈출하는데 필요한 최소 시간(탈출할 수 없다면 -1)
    """
    for i, row in enumerate(maps):
        for j, cell in enumerate(row):
            if cell == 'S':
                begin = (i, j)
            elif cell == 'L':
                lever = (i, j)
            elif cell == 'E':
                end = (i, j)

    # 1. 시작 지점에서 레버가 있는 곳까지 최단 시간(거리) 구하기
    time_to_lever = bfs(maps, begin, lever)
    if time_to_lever == -1:
        return -1

    # 2. 레버에서 출구까지의 최단 시간(거리) 구하기
    time_to_exit = bfs(maps, lever, end)
    if time_to_exit == -1:
        return -1

    return time_to_lever + time_to_exit


if __name__ == '__main__':
    print(solution(maps=["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) # 16
    print(solution(maps=["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) # -1
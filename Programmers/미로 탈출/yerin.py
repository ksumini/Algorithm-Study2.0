'''
5*5 <= size <= 100*100
시작 != 출구 != 레버

1. S --> L : exit and O
2. L --> exit : S and O and L
'''
from collections import deque

def bfs(start: list, target: str, arr: list) -> int:
    """
        :param start: 시작 인덱스 [i, j] 형태
        :param target: 종료 지점 ex) "S"
        :param arr: maps 전달
        :return: 시작 지점부터 종료 지점까지 최단 거리 반
    """

    # 방문 여부를 확인하는 visited 배열 생성
    visited = [[False for _ in range(len(arr[0]))] for _ in range(len(arr))]
    # 시작 지점 방문처리
    visited[start[0]][start[1]] = True
    # 큐에 시작 시점과 거리 정보 삽입 -> ([i, j], 거리)
    q = deque([(start, 0)])

    while q:
        # 현재 인덱스당(row, col)와 거리 변수 할당
        (row, col), dist = q.popleft()
        # 현재 위치가 종료 지점일 때 거리 반환
        if arr[row][col] == target:
            return dist

        # 현재 위치의 좌우상하로 인덱스 업데이트. (조건: maps 안의 좌표 & 최초 방문 & 벽("X")이 아니어야 함)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < len(arr) and 0 <= nc < len(arr[0]) and not visited[nr][nc] and arr[nr][nc] != "X":
                # 방문 처리
                visited[nr][nc] = True
                # 거리 + 1 업데이트
                q.append(((nr, nc), dist + 1))
    # 종료 지점에 도달하지 못하는 경우, -1 반환
    return -1

# 특정 값을 가지는 칸 인덱스 찾는 함
def find_coordinates(maps, target):
    """
    :param maps: maps 전
    :param target: 찾고자 하는 값
    :return: 타겟의 인덱스 반. 타겟이 없는 경우 None 반
    """
    for i, row in enumerate(maps):
        for j, val in enumerate(row):
            if val == target:
                return [i, j]
    return None


def solution(maps):
    # 시작, 라벨 인덱스 할당
    start = find_coordinates(maps, "S")
    label = find_coordinates(maps, "L")

    # 1. [시작 ~ 라벨] 최단 시간. -1일 경우 -1 반환
    dist_to_l = bfs(start, "L", maps)
    if dist_to_l == -1:
        return -1
    # 2. [라벨 ~ 종료] 최단 시간. -1일 경우 -1 반환
    dist_to_exit = bfs(label, "E", maps)
    if dist_to_exit == -1:
        return -1
    # 시작 ~ 라벨 ~ 종료 최단 거
    return dist_to_l + dist_to_exit

# print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))  # Output: 16
# print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))  # Output: -1

"""
start : 2024.03.21 15:30
end : 2024.03.21 16:10

- 그래프 탐색(BFS, DFS)을 활용한 완전탐색으로 풀이
- 각 columns마다 시추관을 꽂아서 몇 칸을 탐색할 수 있는지 탐색(BFS) -> TLE
- 하나의 덩어리 BFS 탐색 시, 해당 지점에 몇 칸 있는지를 명시(Memoization) -> TLE
- 반대로 BFS 탐색때마다 거치게 되는 col에 몇 칸이 있는지를 더해주면 됨 -> 해결
"""
from typing import List
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(r: int,
        c: int,
        matrix: List[List[int]],
        visited: List[List[bool]],
        cols: List[int]) -> None:
    """
    :param r: BFS 시작 행 번호
    :param c: BFS 시작 열 번호
    :param matrix: 격자
    :param visited: 격자 특정 칸 방문장여부
    :param cols: 각 column별 BFS결과 저장
    :return: None

    (r, c)를 시작으로 석유가 있는 칸을 BFS한 결과를 cols에 거치는 column별로 저장한다.
    """

    N, M = len(matrix), len(matrix[0])
    queue = deque([(r, c)])
    visited[r][c] = True
    result = 0

    cols_set = set()    # 해당 BFS가 거치는 column 저장

    while queue:
        y, x = queue.popleft()
        cols_set.add(x)
        result += 1

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < N \
                    and 0 <= nx < M \
                    and not visited[ny][nx] \
                    and matrix[ny][nx] == 1:
                queue.append((ny, nx))
                visited[ny][nx] = True

    # 거치는 column에 BFS 결과 더해주기
    for col in cols_set:
        cols[col] += result

    return


def solution(land: List[List[int]]) -> int:
    N, M = len(land), len(land[0])

    visited = [[False for _ in range(M)] for _ in range(N)]
    cols = [0 for _ in range(M)]    # 각 column별 BFS 결과 저장

    for r in range(N):
        for c in range(M):
            if land[r][c] == 1 and not visited[r][c]:
                bfs(r, c, land, visited, cols)

    return max(cols)    # 최대 결과 column 반환
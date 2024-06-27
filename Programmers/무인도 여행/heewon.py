'''
## 함수 설명
- `dfs`: DFS 방식으로 연결된 섬끼리의 식량의 합 반환

## 접근 방식
- DFS가 접근하기 쉬워서 코드 작성
- 방문 표시를 집합으로 설정하여 빠르게 진행

## 사용한 모듈
`None`

## 추가 정보
- 시간: 20 min 이하
- 힌트: `None`
'''

import sys
limit_num = 100000
sys.setrecursionlimit(limit_num)  # 재귀 제한 깊이 설정 (필요에 따라 조정)


def solution(maps: list) -> list:
    """
    지도 (maps)를 입력받아 각 섬의 일 수를 나타내는 리스트를 반환하는 함수

    Args:
        maps: 2차원 문자열 리스트. 각 원소는 'X' (바다), '1' (육지 1일) ~ '9' (육지 9일) 

    Returns:
        각 섬의 일 수 를 담은 정렬된 리스트, 섬이 없으면 [-1]
    """

    answer = []  # 섬 정보를 담을 리스트
    n = len(maps)  # 지도의 행 수
    m = len(maps[0])  # 지도의 열 수
    visited = set()  # 방문 여부 체크 (집합 사용)

    def dfs(x: int, y: int) -> int:
        """
        깊이 우선 탐색을 이용하여 섬의 크기를 계산하는 함수

        Args:
            x: 현재 위치 (행)
            y: 현재 위치 (열)

        Returns:
            해당 섬의 일 수
        """

        days = int(maps[x][y])  # 현재 위치의 땅 정보 (걸리는 일 수)

        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  # 상, 하, 좌, 우 이동
            xx = x + dx
            yy = y + dy

            if 0 <= xx < n and 0 <= yy < m and maps[xx][yy] != 'X' and (xx, yy) not in visited:
                visited.add((xx, yy))  # 방문 표시
                days += dfs(xx, yy)  # 재귀 호출 (인접한 육지 탐색)

        return days

    # 모든 좌표를 순회하며 방문하지 않은 섬에서 DFS 시작
    for r in range(n):
        for c in range(m):
            if maps[r][c] != 'X' and (r, c) not in visited:
                visited.add((r, c))
                answer.append(dfs(r, c))

    if answer:  # 섬이 존재하면 정렬된 섬 크기 리스트 반환
        return sorted(answer)
    else:  # 섬이 없으면 [-1] 반환
        return [-1]

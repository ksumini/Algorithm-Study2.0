"""
start : 2024.04.07 21:25
end : 2024.04.07 23:25 (2시간 소요)
"""
"""
- 빨간 수레, 파란 수래 -> 시작칸부터 도착칸까지 이동시키면 퍼즐 해결
- 각 턴마다 모든 수레를 상하좌우 인접 한 칸
    - 도착칸 도착한 수레는 움직이지 않음
    - 동시에 두 수레 같은칸 x
    - 자리바꾸기 x
- maximum 4x4 이므로 BFS를 통한 완전탐색으로 풀이 시작
- BFS 시 각 수레의 경로 추적을 위한 별도의 로직 필요 -> DFS 전환
    - 각 분기 별 수레의 경로를 인자로 받아 backtracking으로 해당 분기 경로 추적 가능(line 97~98)
- red 상하좌우 이동에 따른 blue 상하좌우 이동 분기에서 조건을 만족하는 분기만 생성하여 진행하는 방식
"""

from typing import List, Tuple, Set

N, M = 0, 0     # 명시적 초기화
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
answer = 17     # 격자는 최대 4 x 4


def dfs(maze: List[List[int]],                  # 격자
        r_y: int, r_x: int,                     # 해당 분기 빨간 수레 좌표
        b_y: int, b_x: int,                     # 해당 분기 파란 수레 좌표
        red_finish: Tuple[int, int],            # 빨간 수레 도착 지점
        blue_finish: Tuple[int, int],           # 파란 수레 도착 지점
        red_tracking: Set[Tuple[int, int]],     # 해당 분기 빨간 수레 경로
        blue_tracking: Set[Tuple[int, int]],    # 해당 분기 파란 수레 경로
        red_finished: bool,                     # 해당 분기 빨간 수레 도착 여부
        blue_finished: bool,                    # 해당 분기 파란 수레 도착 여부
        cnt: int) -> None:                      # 해당 분기 턴 수

    global answer

    # 최소 해결이 아닌 경우 일찍 케이스 종료
    if answer < cnt:
        return

    # red, blue 모두 도착한 경우 분기 종료
    if red_finished and blue_finished:
        if answer > cnt:
            answer = cnt
        return

    # red 상하좌우에 따른 blue 상하좌우 이동 분기 생성
    for r_d in range(4):
        r_ny = r_y + dy[r_d]
        r_nx = r_x + dx[r_d]

        # 레드 도착 시, 움직이지 않고 고정
        if red_finished:
            r_ny, r_nx = red_finish
        # 도착하지 않은 경우에서 red case 가지치기
        elif not (0 <= r_ny < N and
                  0 <= r_nx < M and
                  (r_ny, r_nx) not in red_tracking and
                  maze[r_ny][r_nx] != 5):
            continue

        for b_d in range(4):
            b_ny = b_y + dy[b_d]
            b_nx = b_x + dx[b_d]

            # 블루 도착 시, 움직이지 않고 고정
            if blue_finished:
                b_ny, b_nx = blue_finish
            # 도착하지 않은 경우에서 blue case 가지치기
            elif not (0 <= b_ny < N and
                      0 <= b_nx < M and
                      (b_ny, b_nx) not in blue_tracking and
                      maze[b_ny][b_nx] != 5):
                continue

            # 동시에 같은 좌표 case 처리
            if (r_ny, r_nx) == (b_ny, b_nx):
                continue
            # red, blue 자리 교환 case 처리
            if (r_ny, r_nx) == (b_y, b_x) and (b_ny, b_nx) == (r_y, r_x):
                continue

            # red 도착한 경우, 도착 여부 업데이트
            if not red_finished and (r_ny, r_nx) == red_finish:
                red_finished = True
            # blue 도착한 경우, 도착 여부 업데이트
            if not blue_finished and (b_ny, b_nx) == blue_finish:
                blue_finished = True

            # 다음 경우로 재귀
            dfs(maze,
                r_ny, r_nx,                             # 다음 분기 빨간 수레 좌표
                b_ny, b_nx,                             # 다음 분기 파란 수레 좌표
                red_finish,
                blue_finish,
                red_tracking.union({(r_ny, r_nx)}),     # 다음 분기 빨간 수레 경로(다음 좌표 포함 - backtracking)
                blue_tracking.union({(b_ny, b_nx)}),    # 다음 분기 파란 수레 경로
                red_finished,
                blue_finished,
                cnt + 1)                                # 다음 분기 턴 수


def solution(maze: List[List[int]]) -> int:
    global N, M
    N, M = len(maze), len(maze[0])
    red_start, blue_start = (0, 0), (0, 0)  # 명시적 초기화
    red_finish, blue_finish = (0, 0), (0, 0)  # 명시적 초기화

    # 수레 출발 좌표, 도착 좌표 탐색
    for r in range(N):
        for c in range(M):
            if maze[r][c] == 1:
                red_start = (r, c)
            elif maze[r][c] == 2:
                blue_start = (r, c)
            elif maze[r][c] == 3:
                red_finish = (r, c)
            elif maze[r][c] == 4:
                blue_finish = (r, c)

    # 최초 분기 생성
    dfs(maze,
        red_start[0], red_start[1],
        blue_start[0], blue_start[1],
        red_finish,
        blue_finish,
        {red_start},
        {blue_start},
        False,
        False,
        0)

    return answer if answer < 17 else 0


def main() -> None:
    case1 = [[1, 4], [0, 0], [2, 3]]
    case2 = [[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]]
    case3 = [[1, 5], [2, 5], [4, 5], [3, 5]]
    case4 = [[4, 1, 2, 3]]

    # print(solution(case1))  # 3
    # print(solution(case2))  # 7
    # print(solution(case3))  # 0
    # print(solution(case4))  # 0


main()

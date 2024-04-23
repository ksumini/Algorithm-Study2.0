"""
https://school.programmers.co.kr/learn/courses/30/lessons/250134
"""


def solution(maze):
    """
    - 약 2시간 풀이 후 실패로 힌트 참조 - 약 3시간 더 풀이 후 실패
    - 두 원이 겹쳐질 때에 대한 예외처리
        - 이동 전과 이동 후의 R, B 순서 바뀌었을 때
        - 두 원을 같은 곳에 이동시킬 때
    - 빨강, 파랑 두 원의 움직임을 병렬적으로 구현할 지, 하나를 먼저 이동시켜놓고 발자취를 기록해놓을지 선택
        - BFS로 구현하면 후자를 선택해야하는데 너무 복잡함
    - 입력 개수가 매우 작으니 가능한 모든 경우를 탐색, 백트래킹을 활용
        - 종료 조건 : 둘 다 정답에 도달 했을 때 탐색 종료
    - 일부 테케에서 통과 못해 힌트 참조 -> 풀이 로직은 거의 똑같은 것 같은데 dx, dy 순서에 따라서 답이 달라짐?!
        - 방문 순서에 따라서 답이 달라진다는 뜻 왜..?
    - 그냥 몇 개 안되니 direction 순열로 다 때려박고 가장 최소값을 정답인 것으로 해결
        - 하려 했으나 테케 7번, 9번에서 실패
    - 반복문에서 빨강 대신 파랑을 먼저 돌리면 테케 7번만 실패..?
    - 뭔가 굉장히 잘못 설계한 것 같은데 도저히 디버깅 불가해서 그냥 이렇게 제출하고 여러분들의 풀이를 공부하겠습니당 .. ㅜㅠ
    """
    from itertools import permutations

    n, m = len(maze), len(maze[0])

    for x in range(n):
        for y in range(m):
            if maze[x][y] == 1:
                red_start = x, y
            elif maze[x][y] == 2:
                blue_start = x, y
            elif maze[x][y] == 3:
                red_end = x, y
            elif maze[x][y] == 4:
                blue_end = x, y

    # 조건에 맞는 움직일 수 있는 좌표 반환하는 함수
    def check_condition(now, end, visited):
        if now == end:  # 정답에 도달했다면 움직이지 않아야 함
            return [end]

        candidates = []

        for dx, dy in direction:
            nx, ny = now[0] + dx, now[1] + dy
            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and maze[nx][ny] != 5  # 벽이 아니여야함
            ):
                candidates.append((nx, ny))

        return candidates

    def dfs(red, blue, cnt):
        nonlocal answer

        if red == red_end and blue == blue_end:
            answer = min(answer, cnt)
            return

        # 현재 좌표에서 움직일 수 있는 좌표 반환
        new_reds = check_condition(red, red_end, red_visited)
        new_blues = check_condition(blue, blue_end, blue_visited)

        for new_blue in new_blues:
            for new_red in new_reds:
                # 둘이 겹치지 않음 and 이전과 순서 바뀌지 않음
                if new_red != new_blue and (new_red, new_blue) != (blue, red):
                    red_visited[new_red[0]][new_red[1]] = True
                    blue_visited[new_blue[0]][new_blue[1]] = True
                    dfs(new_red, new_blue, cnt + 1)

    answer = 1e9

    # 방문 순서에 따라서 정답이 달라져서 방문 순서 순열 돌린 후 최소값으로 정답 계산
    for direction in permutations([(0, 1), (1, 0), (0, -1), (-1, 0)]):
        red_visited = [[False for _ in range(m)] for _ in range(n)]
        blue_visited = [[False for _ in range(m)] for _ in range(n)]

        red_visited[red_start[0]][red_start[1]] = True
        blue_visited[blue_start[0]][blue_start[1]] = True

        dfs(red_start, blue_start, 0)

    return answer if answer != 1e9 else 0

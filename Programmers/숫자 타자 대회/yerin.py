'''
숫자로만 이루어진 문자열
민희 : 두 엄지 손가락
[4, 6]

가중치
- 제자리 : 1
- 상하좌우 : 2
- 대각선 : 3
- 그 외: 경로별 가중치 합 최소

양손 동일한 숫자 위에 있을 수 없음
'''
from collections import deque, defaultdict


# 상하좌우, 대각선, 동일한 위치에 있는 경우가 아닌 경우, 최소 거리를 구해주는 함수
def measure_distance(start, end):
    n, m = 4, 3
    q = deque([(start, 0)])
    diagonal = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    visited = set()
    ex, ey = end

    while q:
        (x, y), dist = q.popleft()

        if (x, y) == (ex, ey):
            return dist

        # 탐색하는 경로 줄이기
        if x == ex:  # 목표 지점이 현재 위치와 같은 행
            directions = [(0, 1), (0, -1)]
        elif x < ex:  # 목표 지점이 현재 위치보다 아래에 있을 때
            directions = [(1, 0), (1, 1), (1, -1)]
        else:  # 목표 지점이 현재 위치보다 위에 있을 때
            directions = [(-1, 0), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                visited.add((nx, ny))
                if (dx, dy) in diagonal:
                    q.append(((nx, ny), dist + 3))
                else:
                    q.append(((nx, ny), dist + 2))

# 경로 계산
def cost(start, end):
    sx, sy = start
    ex, ey = end

    if start == end:  # 동일
        return 1
    elif abs(sx - ex) + abs(sy - ey) == 1:  # 상하좌우
        return 2
    elif abs(sx - ex) == 1 and abs(sy - ey) == 1:  # 대각선
        return 3
    else:  # 그 외
        return measure_distance(start, end)


def solution(numbers):
    # 숫자판 위치 설정
    pos = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2),
        '*': (3, 0), '0': (3, 1), '#': (3, 2)
    }

    # 모든 경로에 대한 거리값 미리 구해놓음
    dist = defaultdict(int)
    for i in range(4):
        for j in range(3):
            for num in range(10):
                dist[(i, j), pos[str(num)]] = cost((i, j), pos[str(num)])

    left = pos['4']
    right = pos['6']
    dp = {(left, right): 0}  # (왼손 좌표, 오른손 좌표, 누적 거리)

    for num in numbers:
        num_pos = pos[num]
        new_dp = {}  # 다음 숫자로 넘어갈 때마다 dp를 갱신하기 위한 변수

        for (l_pos, r_pos), cur_dist in dp.items():
            if l_pos == r_pos:  # 왼손 오른손 겹치는 경우 제외
                continue

            if l_pos == num_pos:  # 숫자의 좌표와 왼손 위치 동일
                new_dp[(num_pos, r_pos)] = cur_dist + 1
            elif r_pos == num_pos:  # 숫자의 좌표와 오른손 위치 동일
                new_dp[(l_pos, num_pos)] = cur_dist + 1
            else:  # 왼손, 오른손, 숫자 모두 다른 좌표
                # 이미 new_dp에 있는 경우, 출발지에 따라 거리값이 다를 수 있으니 최솟값으로 갱신
                # 왼손이 이동
                if (num_pos, r_pos) in new_dp and new_dp[(num_pos, r_pos)] < cur_dist + dist[(l_pos, num_pos)]:
                    pass
                else:
                    new_dp[(num_pos, r_pos)] = cur_dist + dist[(l_pos, num_pos)]
                # 오른손이 이동
                if (l_pos, num_pos) in new_dp and new_dp[(l_pos, num_pos)] < cur_dist + dist[(r_pos, num_pos)]:
                    pass
                else:
                    new_dp[(l_pos, num_pos)] = cur_dist + dist[(r_pos, num_pos)]
        dp = new_dp
    return min(dp.values())

# print(solution('4'))
# print(solution('6'))
# print(solution('46'))
# print(solution('4666666'))
# print(solution("1756"))
# print(solution("5123"))
# print(solution('1111'))
# print(solution('486'))
# print(solution("2580"))
# print(solution("3692581470"))
# print(solution("7531"))
print(solution("12345"))
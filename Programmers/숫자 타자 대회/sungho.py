from collections import defaultdict
from collections import deque
import heapq as hq

LOCATIONS = {}  # LOCATIONS[숫자판] = [y,x]


def set_loc():
    """
    LOCATIONS[숫자판] = [y,x] 으로 숫자판 dictionary로 저장
    ['1'] = [0,0] ...
    """
    global LOCATIONS
    for i in range(1, 10):
        LOCATIONS[str(i)] = [(i - 1) // 3, (i - 1) % 3]
    LOCATIONS['*'] = [3, 0]
    LOCATIONS['0'] = [3, 1]
    LOCATIONS['#'] = [3, 2]
    return None


def set_w():
    """
    LOCATIONS[숫자판] = [y,x] 으로 숫자판 dictionary로 저장된 것을 이용해
    weight_dict[시작점, 도착점] = 가중치 저장하는 판
    """
    global LOCATIONS
    weight_dict = {}  # [시작, 끝] = weight
    for i in range(10):  # 0 ~ 9
        for j in range(i, 10):
            num1, num2 = i, j
            loc1, loc2 = LOCATIONS[str(i)], LOCATIONS[str(j)]
            weight = cal_w(loc1, loc2)
            weight_dict[(str(num1), str(num2))] = weight
            weight_dict[(str(num2), str(num1))] = weight
        loc1, loc2 = LOCATIONS['*'], LOCATIONS[str(i)]
        weight = cal_w(loc1, loc2)
        weight_dict[('*', str(i))] = weight
        weight_dict[(str(i), '*')] = weight

        loc1, loc2 = LOCATIONS['#'], LOCATIONS[str(i)]
        weight = cal_w(loc1, loc2)
        weight_dict[('#', str(i))] = weight
        weight_dict[(str(i), '#')] = weight
    return weight_dict


def cal_w(loc1: list, loc2: list) -> int:
    """
    loc1과 loc2 사이의 가중치 구하기
    같으면 가중치 1
    상하좌우로 인접하면 2
    대각선이면 3
    그것보다 더 멀면 최소로 움직일 수 있는 경로로 가중치
    """
    dis_y = abs(loc1[0] - loc2[0])
    dis_x = abs(loc1[1] - loc2[1])

    diag_mov = min(dis_y, dis_x)  # 대각선 이동
    next_mov = max(dis_y, dis_x) - diag_mov  # 상하좌우 이동

    if dis_y == dis_x and dis_y == 0:  # 제자리 눌러야함
        return 1
    return diag_mov * 3 + next_mov * 2


def solution(numbers: str) -> int:
    """
    numbers를 치는데 가장 작은 가중치를 반환하는 함수
    """
    global LOCATIONS
    answer = float("inf")

    # set number locations
    set_loc()

    # set weight
    weight_dict = set_w()

    dp = defaultdict(lambda: float("inf"))  # dp(L, R, idx) = weight #뒤에 idx 처리해야함
    # using bfs. compare all ways
    L = '4';
    R = '6';
    w = 0;
    idx = 0
    n = len(numbers)
    heap = []
    hq.heappush(heap, (0, L, R, 0))  # (w, L, R, idx)

    while heap:
        w, L, R, idx = hq.heappop(heap)
        if idx == n:  # 가장 작은 weight로 끝까지 다 왔음
            answer = w
            break

        n_num = numbers[idx]
        n_loc = LOCATIONS[n_num]

        L_mov = weight_dict[(L, n_num)]
        R_mov = weight_dict[(R, n_num)]

        # dp(L, R, idx) = weight #뒤에 idx 처리해야함
        if min(L_mov, R_mov) == 1:  # L이나 R이 그 수 위에 있으면 반드시 그 손가락으로 눌러야함
            dp[(L, R, idx + 1)] = min(w + 1, dp[(L, R, idx + 1)])
            hq.heappush(heap, (w + 1, L, R, idx + 1))
            continue

        if dp[(n_num, R, idx + 1)] > w + L_mov:  # L 이동 (L이 그 숫자 위에 있는게 아님)
            dp[(n_num, R, idx + 1)] = w + L_mov
            hq.heappush(heap, (w + L_mov, n_num, R, idx + 1))
        if dp[(L, n_num, idx + 1)] > w + R_mov:  # R 이동 (R이 그 숫자 위에 있는게 아님)
            dp[(L, n_num, idx + 1)] = w + R_mov
            hq.heappush(heap, (w + R_mov, L, n_num, idx + 1))

    return answer
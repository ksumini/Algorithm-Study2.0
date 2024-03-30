"""
start : 2024-03-27 21:15
end : 3시간 풀이 후 FAIL, 모든 예외 처리 불가
"""
"""
초침이 시침, 분침과 겹칠 때 알람
"""

s_limit = 60
m_limit = 60 * 60
h_limit = 12 * 60 * 60


def get_loc(smh: int, limit: int) -> float:
    """
    초/분/시침의 각도 계산
    """
    return smh/limit


def is_min_dup(s: int, m: int) -> bool:
    """
    초침과 분침이 역전하는 지 확인하여 만났는지 여부를 판단
    """
    return get_loc(s, s_limit) < get_loc(m, m_limit) and (s+1 == 60 or get_loc(s+1, s_limit) > get_loc(m+1, m_limit))


def is_hour_dup(s: int, h: int) -> bool:
    """
    초침과 시침이 역전하는 지 확인하여 만났는지 여부를 판단
    """
    return get_loc(s, s_limit) < get_loc(h, h_limit) and (s+1 == 60 or get_loc(s+1, s_limit) > get_loc(h+1, h_limit))


def solution(h1: int, m1: int, s1: int,
             h2: int, m2: int, s2: int) -> int:

    s = s1
    m = 60 * m1 + s         # 분 -> 초
    h = 60 * 60 * h1 + m    # 시 -> 초

    cnt = 0

    if get_loc(s, s_limit) == get_loc(m, m_limit):
        cnt += 1
    if get_loc(s, s_limit) == get_loc(h, h_limit):
        cnt += 1

    for _ in range((s2+60*m2+60*60*h2)-h):
        # 초, 분, 시침이 동시에 만나는 경우
        if is_min_dup(s, m) and is_hour_dup(s, h):
            cnt += 1
            continue
        # 초침과 분침이 만나는 경우
        if is_min_dup(s, m):
            cnt += 1
        # 초침과 시침이 만나는 경우
        if is_hour_dup(s, h):
            cnt += 1

        s = (s+1) % s_limit
        m = (m+1) % m_limit
        h = (h+1) % h_limit

    return cnt


def main():
    case1 = [0, 5, 30, 0, 7, 0]  # 2
    case2 = [12, 0, 0, 12, 0, 30]    # 1
    case3 = [0, 6, 1, 0, 6, 6]   # 0
    case4 = [11, 59, 30, 12, 0, 0]   # 1
    case5 = [11, 58, 59, 11, 59, 0]  # 1
    case6 = [1, 5, 5, 1, 5, 6]  # 2
    case7 = [0, 0, 0, 23, 59, 59]   # 2852

    print(solution(*case1))
    print(solution(*case2))
    print(solution(*case3))
    print(solution(*case4))
    print(solution(*case5))
    print(solution(*case6))
    print(solution(*case7))


main()

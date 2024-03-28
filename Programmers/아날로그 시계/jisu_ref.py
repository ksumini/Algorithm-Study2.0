"""
솔루션 참고
[ref1](https://school.programmers.co.kr/questions/71323)
[ref2](https://school.programmers.co.kr/questions/64706)
초/분/시침 위치 기반 접근이 아닌, 수리적 접근??
"""


def count_alarm(sec: int) -> int:
    """
    시침 : 1 바퀴 / 12시간(43200초)
    초침 : 720 바퀴 / 12시간
    43200초 동안 719번 울림 -> 43200/719초 마다 1회 울림

    분침 : 1바퀴 / 1시간(3600초)
    초침 : 60바퀴 / 1시간
    3600초 동안 59번 울림 -> 3600/59초 마다 1회 울림

    00시 및 12시 정각에는 시-분-초 동시에 알람이 울리므로, 1회 페널티
    -> 12시간 이상인 경우 2회 페널티, 아닌 경우 1회 페널티
    """
    h_alram = sec * 719 // 43200
    m_alram = sec * 59 // 3600

    penalty = 2 if 43200 <= sec else 1

    return h_alram + m_alram - penalty


def is_alram_at_start(sec: int) -> bool:
    """
    시작 시점에 분-초, 시-초침이 일치하는 경우
    """
    return sec * 719 % 43200 == 0 or sec * 59 % 3600 == 0


def solution(h1: int, m1: int, s1: int,
             h2: int, m2: int, s2: int) -> int:

    time_to_sec_2 = 3600 * h2 + 60 * m2 + s2
    time_to_sec_1 = 3600 * h1 + 60 * m1 + s1

    result = count_alarm(time_to_sec_2) - count_alarm(time_to_sec_1)

    return result+1 if is_alram_at_start(time_to_sec_1) else result


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

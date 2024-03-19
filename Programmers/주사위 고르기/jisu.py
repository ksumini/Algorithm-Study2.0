"""
start : 2024.03.19 10:40
end : 2024.03.19 12:30(ref. https://school.programmers.co.kr/questions/66170)

승리할 확률이 가장 높은 조합이 유일한 완탐(+ 이분탐색)

1. 주사위 n개중 n//2를 뽑는 모든 조합 찾기 : make_combinations()
    - A주사위, B주사위 조합 나누기
2. n//2개의 주사위를 굴리는 모든 경우의 수 찾기 : product()
3. (모든 주사위 조합 + 굴리는 모든 경우의 수)에 따른 결과 구하기 : get_roll_result()
    - A주사위 결과, B주사위 결과
4. A, B 주사위 결과에 따른 승리 횟수 구하기 : get_wins_cnt()
    - 이 경우 A, B 주사위 결과를 완탐하여 승리 횟수를 구하게 되면 TLE 발생
    - ref를 참고하여 이분탐색으로 접근
        - B 결과에 대한 A의 모든 요소의 lower bound = A의 요소가 B에서 승리하는 횟수
        - n^2 -> nlogn으로 개선

+) 조합을 구할 때 itertools의 permutation과 product를 사용하면 비교적 간단하게 구현 가능 (삼성 SW 역량평가 대비 직접 구현함)
"""

from typing import List, Set


def make_combinations(n: int, k: int) -> List[Set]:
    """
    주사위 n개(0~n-1) 중 k개를 뽑는 조합 반환
    ex) 주사위 4개 중 2개를 뽑기
    [0, 1], [0, 2], ...,  [2, 3]
    """
    result = []

    def recur(tmp):
        if len(tmp) == k:
            result.append(set(tmp))
            return

        for i in range(n):
            if not tmp or i > tmp[-1]:
                recur(tmp + [i])

    recur([])

    return result


def product(n: int) -> List[List[int]]:
    """
    주사위 n개를 굴리는 경우의 수(인덱스 조합) 반환
    ex) 주사위 3개인 경우
    [0, 0, 0] ~ [5, 5, 5] 반환
    """
    result = []

    def recur(tmp: List) -> None:
        if len(tmp) == n:
            result.append(tmp)
            return

        for i in range(6):
            recur(tmp + [i])

    recur([])

    return result


def get_roll_result(dice: List[List[int]], products: List[List[int]], picks: Set[int]) -> List[int]:
    """
    주사위 pick에 따른 점수의 합의 모든 경우의 수 반환
    ex) [0, 1]번 주사위가 각각 [2, 3]번 면이 나왔을 때의 합
    """
    result = []
    for indice in products:
        tmp_sum = 0
        for idx, dice_idx in zip(indice, picks):
            tmp_sum += dice[dice_idx][idx]
        result.append(tmp_sum)

    return result


def get_wins_cnt(A: List[int], B: List[int]) -> int:
    """
    모든 주사위 점수의 합에 따른 승리 횟수 반환(이분탐색 활용)
    """
    result = 0

    A.sort()
    B.sort()

    for a in A:
        # B 리스트에 대한 a의 lower bound(찾고자 하는 값 이상이 처음 나타나는 위치)
        # = a가 몇 개의 경우의 수를 이기는지 개수
        start, end = 0, len(B) - 1

        while start <= end:
            mid = (start + end) // 2
            if a > B[mid]:
                start = mid + 1
            else:
                end = mid - 1

        result += end

    return result


# def get_wins_cnt(A: List[int], B: List[int]) -> int:
#     """
#     모든 주사위 점수의 합에 따른 승리 횟수 반환(TLE 발생)
#     """
#     result = 0

#     for a in A:
#         for b in B:
#             if a > b:
#                 result += 1

#     return result


def solution(dice: List[List[int]]) -> List[int]:
    n = len(dice)
    combinations = make_combinations(n, n // 2)  # 주사위 조합
    products = product(n // 2)  # 주사위 면의 조합

    answer_cnt = 0
    answer = None   # 명시적 초기화

    for A_picks in combinations:
        B_picks = set(range(n)) - A_picks

        A_picks_result = get_roll_result(dice, products, A_picks)  # A 주사위 결과
        B_picks_result = get_roll_result(dice, products, B_picks)  # B 주사위 결과

        wins_cnt = get_wins_cnt(A_picks_result, B_picks_result)  # A 주사위가 이긴 횟수

        if answer_cnt < wins_cnt:   # answer 업데이트
            answer_cnt = wins_cnt
            answer = sorted(list(map(lambda x: x + 1, A_picks)))    # 인덱스가 1부터 시작함, 오름차순

    return answer

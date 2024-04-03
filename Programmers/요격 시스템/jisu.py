"""
start : 2024.04.03 22:15
end : 2024.04.03 22:30
"""
"""
1 <= targets <= 500,000
0 <= s < e <= 100,000,000

- 완전탐색 불가, 로직이 필요
1. 폭발 범위 끝 기준으로 오름차순 정렬
2. 가장 끝에서 폭발(e가 가장 큰)하는 s를 기준, 범위가 겹치는 폭발(기준 s보다 큰 e)을 계속 pop() -> 동시 요격 가능
    2-1. 이 때 범위가 겹치는 폭발에서 s가 더 크면 기준 s를 업데이트 (동시 요격 가능한 추가 폭발)
    2-2. 더 이상 기준 s보다 큰 e를 가진 폭발이 없으면 새로 쏴야 함 -> 해당 폭발을 기준으로 다시 1로 돌아감
"""
from typing import List


def solution(targets: List[List[int]]) -> int:
    """
    :param targets: 각 폭격 미사일의 x 좌표 범위 목록
    :return: 모든 폭격 미사일을 요격하기 위해 필요한 요격 미사일 수의 최솟 값
    """

    targets.sort(key=lambda x: x[1])    # 폭발 범위 끝 기준으로 오름차순 정렬
    answer = 0

    while targets:
        standard = targets.pop()[0]     # 가장 끝에서 폭발(e가 가장 큰)하는 s를 기준

        while targets and targets[-1][1] > standard:    # 범위가 겹치는 폭발(기준 s보다 큰 e)을 계속 pop() -> 동시 요격 가능
            standard = max(standard, targets.pop()[0])  # 이 때 범위가 겹치는 폭발에서 s가 더 크면 기준 s를 업데이트
        answer += 1

    return answer


def main() -> None:
    case1 = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

    print(solution(case1))  # 3


main()
"""
<문제>
n개의 퍼즐을 제한 시간 내에 풀어야 한다.
각 퍼즐은 난이도와 소요시간이 정해져있다.
숙련도에 따라 퍼즐을 풀 때 틀리는 횟수가 바뀐다.

diff <= level : 퍼즐을 틀리지 않고 time_cur만큼 사용
diff > level : 퍼즐을 diff - level번 틀린다. 틀릴때마다 time_cur만큼의 시간을 사용, 추가로 time_prev만큼 시간을 사용해 이전 퍼즐을 풀어야한다.
이전 퍼즐을 풀 때는 이전 퍼즐의 난이도와 상관없이 틀리지 않는다.

<풀이>
풀이 시간: 30분
- 이진 탐색으로 가능한 최소 숙련도를 찾는다
- 주어진 숙련도로 모든 퍼즐을 푸는데 걸리는 시간 계산

<시간 복잡도>
"""

from typing import List


def calculate_time(level: int, diffs: List, times: List) -> int:
    """
    주어진 숙련도(level)로 모든 퍼즐을 푸는데 걸리는 총 시간을 계산
    """
    total_time = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            # 숙련도가 난이도보다 높거나 같으면 한 번에 해결
            total_time += times[i]
        else:
            # 숙련도가 난이도보다 낮으면 여러 번 시도
            mistakes = diffs[i] - level  # 실수하는 횟수
            if i > 0:
                # 실수할 때마다 현재 퍼즐 시간 + 이전 퍼즐 다시 풀기 시간이 필요
                total_time += (times[i] + times[i-1]) * mistakes
            total_time += times[i]  # 마지막 성공 시도
    return total_time


def solution(diffs: List, times: List, limit: int) -> int:
    """
    :param diffs: 퍼즐의 난이도를 순서대로 담은 1차원 정수 배열
    :param times: 퍼즐의 소요 시간을 순서대로 담은 1차원 정수 배열
    :param limit: 전체 제한 시간
    :return: 제한 시간 내에 퍼즐을 모두 해결하기 위한 숙련도의 최솟값
    """
    # 이분 탐색 설정
    left = 1  # 최소 가능한 숙련도
    right = max(diffs)  # 최대 가능한 숙련도

    result = right  # 초기값을 최대값으로 설정

    while left <= right:
        mid = (left + right) // 2
        total_time = calculate_time(mid, diffs, times)

        if total_time <= limit:
            # 현재 숙련도로 제한 시간 내에 해결 가능
            result = min(result, mid)
            right = mid - 1  # 더 낮은 숙련도 탐색
        else:
            # 제한 시간을 초과함
            left = mid + 1  # 더 높은 숙련도 탐색

    return result
"""
start : 2024-04-17 16:55
end : 2024-04-17 17:20

- 오름차순 정렬
- 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분수열 구하기
- 부분 수열의 합은 k, 여러개인 경우 길이가 짧고, 앞쪽에 있는 수열

- 투포인터 냄새가 솔솔 나쥬?
- 매번 sum을 구하면 연산량이 너무 큼 -> weighted_sum으로 합계 관리
    - 초기 left 0 / right 0 으로 세팅 (k가 sequence[0]인 엣지케이스)
    - weighted_sum < k 인 경우 right를 늘려 수를 하나 합산
    - weighted_sum > k 인 경우 left를 늘려 왼쪽 수를 하나 제거
"""
from typing import List


def solution(sequence: List[int], k: int) -> List[int]:
    left, right = 0, 0
    weighted_sum = sequence[0]
    min_length = 1000001        # 최대 길이로 초기화
    answer = []                 # 명시적 초기화

    while left <= right:
        # 동일 length라면 먼저 w_sum == k인 경우가 답
        # 답을 찾아도, 이후에 더 짧은 length 고려를 위해 계속 진행해야 함
        if weighted_sum == k and right - left + 1 < min_length:
            answer = [left, right]
            min_length = right - left + 1

        # 부분 수열 합이 더 작은 경우 오른쪽 수 포함시키기
        if weighted_sum < k:
            right += 1

            # 리스트 끝에 다다른경우 더이상 답은 될 수 없음
            if right >= len(sequence):
                break
            weighted_sum += sequence[right]

        # 부분 수열 합이 더 큰 경우 왼쪽 수 제거시키기
        else:
            weighted_sum -= sequence[left]
            left += 1

    return answer
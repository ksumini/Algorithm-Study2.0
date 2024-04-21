'''
## 함수 설명
- `get_waiting_time`: 특정 수의 컨설턴트가 요청 목록을 처리하는 경우의 총 대기 시간을 계산

## 접근 방식
- 처음 접근 방법
    - 모두가 1명일 때의 대기 시간을 구하고 각각의 1명이 증가할 때마다 줄어드는 시간이 가장 큰 경우 제거 ex) 추가시 1유형: 2시간, 2유형: 3시간, 3유형: 1시간이 줄으면 2유형 상담사 추가
    - but 추가시 1유형: 2시간, 2유형: 2시간, 3유형: 1시간 인 경우는 1유형, 2유형 모두 고려해야 함
    - 그리디로 접근하면 X
- 최종 풀이
    - 컨설턴트가 가능한 모든 경우들을 확인하자!
        - x_1 + x_2 + ... + x_k = n (x_i는 자연수)를 만족하는 모든 쌍 구하기
        - 1 <= x_i <= n - k + 1
        - 중복 순열로 가능한 (x_1, x_2, ..., x_n)의 경우를 구하고
        - x_1 + x_2 + ... + x_k = n를 확인하여 만족하는 경우 찾기
    - 상담가 수에 따른 대기 시간 구하기
        - 상담이 가능하면 종료 시간을 기록한다.
        - 상담이 불가능하면 빨리 끝나는 종료 시간을 구하여 대기 시간 추가하고 종료 시간 추가
            - remove로 구현, heap 자료 구조 비슷한 시간이 걸림
    - 중복 계산을 줄이기 위하여 DP table(=waiting_times) 사용
        - row: 상담 유형
        - col: 상담사 수

## 사용한 모듈
`defaultdict`, `product`, `List`, `heapq`

## 추가 정보
- 시간: 1 hour
- 힌트: `None`

### ISSUE NUMBER
<!-- 이슈 번호를 입력해주세요 -->
- #53
'''

# 유형별 나누고 대기 구하고 다음 대기 구하고 최소 구하기
from collections import defaultdict
from itertools import product
import heapq
from typing import List

def solution(k:int, n:int, reqs:List)->int:
    """
    이 함수는 k명의 상담 유형이 n개의 요청을 처리하는 경우의 최소 총 대기 시간을 찾습니다.

    Args:
        k: 상담 유형의 수
        n: 총 요청 수
        reqs: 요청 목록, 리스트 [시작 시간, 지속 시간, 상담 유형]으로 표현됨

    Returns:
        모든 요청에 대한 최소 총 대기 시간
    """
    answer = float('INF')
    # 2D DP 테이블 초기화, 각 셀은 최소 대기 시간을 저장 (초기에는 모두 -1)
    waiting_times = [[-1 for _ in range(n)] for _ in range(k)]

    # 상담 종류별 요청 그룹화를 위한 사전 생성
    consultant_requests = defaultdict(list)
    for start_time, duration, consultant_type in reqs:
        consultant_requests[consultant_type].append([start_time, duration])

    # 기본 사례 처리: 상담 수가 종류 수와 같을 때 (k == n)
    if k == n:
        # 모든 요청이 서로 다른 컨설턴트가 처리하기 때문에 최소 대기 시간은 0
        products = [[1 for _ in range(k)]]  # 모두 1인 제품
    else:
        # 1부터 n k개의 요소를 선택하여 상담 할당의 모든 가능한 조합 생성
        products = product(range(1, n - k + 2), repeat=k)

    # 모든 가능한 상담 할당 조합 반복
    for consultant_assignment in products:
        # 조합이 모든 n개의 요청을 처리하는지 확인 (할당된 컨설턴트의 합이 n과 같음)
        if sum(consultant_assignment) == n:
            total_time = 0
            # 할당된 요청을 가진 각 상담 종류에 대한 대기 시간 계산
            for idx, consultant_requests_count in enumerate(consultant_assignment):
                # 이 상담 종류에 대한 대기 시간이 DP 테이블에 이미 계산되었는지 확인
                if waiting_times[idx][consultant_requests_count-1] == -1:
                    # 계산되지 않았다면 대기 시간을 얻기 위해 함수 호출
                    waiting_times[idx][consultant_requests_count-1] = get_waiting_time(consultant_requests_count, consultant_requests[idx+1])
                # 이 상담 종류에 대한 대기 시간을 총 시간에 추가
                total_time += waiting_times[idx][consultant_requests_count-1]

            # 지금까지 찾은 최소 총 대기 시간으로 답변 업데이트
            answer = min(answer, total_time)

    # 모든 요청에 대한 최소 총 대기 시간 반환
    return answer


def get_waiting_time(available_consultants: int, requests: List[List]) -> int:
    """
    특정 수의 컨설턴트가 요청 목록을 처리하는 경우의 총 대기 시간을 계산합니다.

    Args:
        available_consultants (int): 사용 가능한 상담 수
        requests (List[List]): 이 상담 종류에 대한 요청 목록, 각 요청은 [시작 시간, 지속 시간] 리스트로 표현

    Returns:
        int: 이 상담 종류가 처리하는 모든 요청에 대한 총 대기 시간
    """

    total_waiting_time = 0
    # 현재 처리 중인 요청의 종료 시간 저장
    request_end_times = []

    for start_time, duration in requests:
        new_request_end_times = []
        # 현재 처리 중인 요청 종료 시간과 비교하여 새로운 요청 시작 가능 여부 확인
        for time in request_end_times:
            if start_time >= time:
                # 새로운 요청이 시작될 수 있으므로 사용 가능한 상담 수 증가
                available_consultants += 1
            else:
                # 새로운 요청이 시작될 수 없으므로 기존 요청 종료 시간 유지
                heapq.heappush(new_request_end_times, time)
                # new_request_end_times.append(time)
        # 요청 종료 시간 목록 업데이트
        request_end_times = new_request_end_times

        # 사용 가능한 컨설턴트가 있는 경우
        if available_consultants > 0:
            # 새로운 요청 종료 시간 추가
            heapq.heappush(request_end_times, start_time + duration)
            # request_end_times.append(start_time + duration)
            # 새로운 요청 시작으로 인해 사용 가능한 상담 수 감소
            available_consultants -= 1
        else:
            # 사용 가능한 컨설턴트가 없는 경우
            # 가장 빠른 요청 종료 시간 계산
            earliest_end_time = request_end_times[0]
            # earliest_end_time = min(request_end_times)
            # 총 대기 시간에 가장 빠른 요청 종료 시간과 현재 요청 시작 시간 차 계산
            total_waiting_time += earliest_end_time - start_time
            # 가장 빠른 요청 종료 시간 제거 및 새로운 요청 종료 시간 추가
            heapq.heappop(request_end_times)
            heapq.heappush(request_end_times, earliest_end_time + duration)
            # request_end_times.remove(earliest_end_time)
            # request_end_times.append(earliest_end_time + duration)

    # 이 상담 종류가 처리하는 모든 요청에 대한 총 대기 시간 반환
    return total_waiting_time
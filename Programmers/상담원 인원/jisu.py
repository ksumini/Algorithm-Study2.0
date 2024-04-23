"""
start : 2024-04-23 10:00
end : 2024-04-23 12:30

- 초기 멘토 구성 : 1 / 1 / 1
- 다음 요청에 대기가 가장 많이 필요한 유형의 멘토 증가 => 어느 시점에 대기가 많이 필요한지 예측 불가
- 그럼 모든 요청을 처리했을 때 대기 시간이 가장 많이 필요한 유형의 멘토 증가
    - 최대 멘토는 20명, reqs의 길이는 300이므로 충분히 가능할 듯
    - 모든 테케 예외 처리 불가
- 그리디하게 풀이하려면 증가 시켰을 때, 대기시간이 가장 많이 감소하는 유형을 증가시키는 게 맞음
"""
from typing import List, Deque, Tuple, Set
from collections import deque
from heapq import heappush, heappop
from copy import deepcopy


def get_waiting_time(mentor_heap: List[List[int]],
                     req_queue: List[Deque[Tuple[int, int]]],
                     k: int) -> int:
    """
    :param mentor_heap: 각 유형의 멘토들의 상담 끝나는 시간을 관리할 heap
    :param req_queue: 상담 요청 큐
    :param k: 유형 수
    :return: 현재 인원으로 상담을 돌렸을 때 total waiting time
    """
    total_waiting_time = 0

    for idx in range(1, k + 1):
        waiting_time = 0
        for st, time in req_queue[idx]:
            # 멘토가 바로 상담 가능하지 않은 경우 대기시간 발생
            if mentor_heap[idx][0] > st:        # heap의 첫번째 원소는 가장 빨리 상담할 수 있는 멘토
                waiting_time += mentor_heap[idx][0] - st

            end_time = heappop(mentor_heap[idx])
            st = max(st, end_time)  # 다음 상담 시작 시간 업데이트(상담 대기로 늦어지는 경우 고려)
            heappush(mentor_heap[idx], st + time)

        total_waiting_time += waiting_time

    return total_waiting_time


def get_max_decrease_mentor_idx(mentor_heap: List[List[int]],
                                waiting_time_table: List[int],
                                req_queue: List[Deque[Tuple[int, int]]],
                                valid_types: Set[int],
                                k: int) -> int:
    """
    :param mentor_heap: 각 유형의 멘토들의 상담 끝나는 시간을 관리할 heap
    :param waiting_time_table: 멘토 증가에 따른 최종 대기시간 table
    :param req_queue: 상담 요청 queue
    :param valid_types: 요청이 존재하는 상담 유형
    :param k: 유형 수
    :return: 멘토를 한 명 증가시켰을 때 가장 많은 대기시간이 줄어드는 유형 idx
    """
    max_decrease_mentor_idx = 0
    max_decrease_waiting_time = 0

    for type_ in valid_types:
        tmp_mentor_heap = deepcopy(mentor_heap)
        tmp_mentor_heap[type_] += [0]  # 멘토 증가시켜보기

        result = get_waiting_time(tmp_mentor_heap, req_queue, k)
        # 가장 대기시간이 많이 줄어드는 유형 찾기
        if waiting_time_table[-1] - result > max_decrease_waiting_time:
            max_decrease_mentor_idx = type_
            max_decrease_waiting_time = waiting_time_table[-1] - result

    # 해당 대기시간 table에 반영
    waiting_time_table.append(waiting_time_table[-1] - max_decrease_waiting_time)
    return max_decrease_mentor_idx


def solution(k: int, n: int, reqs: List[List[int]]) -> int:
    num_of_mentor = k
    req_queue = [deque() for _ in range(k + 1)]  # 각 상담 요청에 대한 큐
    mentor_heap = [[0] for _ in range(k + 1)]  # 각 유형 별 멘토 초기 배치
    valid_types = set()

    for st, time, type_ in reqs:
        req_queue[type_].append((st, time))
        valid_types.add(type_)

    # 초기 대기 시간 테이블
    waiting_time_table = [get_waiting_time(deepcopy(mentor_heap), req_queue, k)]

    while num_of_mentor < n:
        # 증가시켰을 때 가장 대기시간이 많이 줄어드는 유형의 멘토 찾기
        idx = get_max_decrease_mentor_idx(deepcopy(mentor_heap),
                                          waiting_time_table,
                                          req_queue,
                                          valid_types,
                                          k)

        mentor_heap[idx].append(0)  # 해당 멘토 한 명 추가
        num_of_mentor += 1

    return waiting_time_table[-1]

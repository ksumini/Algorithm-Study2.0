"""
start : 2024-04-24 18:37
end : 2024-04-24 19:30

- 과제를 시작하기로 한 시각이 되면 시작
- 새로운 과제를 시작할 시각이 되었을 때, 기존 진행 중 과제 멈추고 새로운 과제 시작  -> heap 구현
- 끝냈을 때, 멈춘 과제가 있다면 멈춰둔 과제 이어서 진행                       -> 멈춘 과제는 queue로 관리
- 멈춰둔 과제가 여러 개일 경우, 가장 최근 멈춘 과제부터 시작                   -> 멈추게 되는 경우 appendleft로 앞으로 삽입 (중요)
"""
from typing import List
from collections import deque
from heapq import heappush, heappop


def hhmm2m(hhmm: str) -> int:
    """
    :param hhmm: hh:mm 형식의 문자열 시간
    :return: 전부 분으로 변환한 정수 시간
    """
    hhmm = hhmm.split(':')
    return int(hhmm[0]) * 60 + int(hhmm[1])


def solution(plans: List[str]) -> List[str]:
    subject_heap = []  # min heap (시작 시간, 걸리는 시간, 과목)
    post_queue = deque()  # 미뤄둔 과제에 대한 큐 (남은 시간, 과목)

    for subject, hhmm, time in plans:
        heappush(subject_heap, [hhmm2m(hhmm), int(time), subject])

    ing = [0, 0, '']  # dummy data (시작시간, 걸리는 시간, 과목))
    answer = []

    while subject_heap:
        start, time, subject = ing         # (시작시간, 걸리는 시간, 과목)
        term = subject_heap[0][0] - start  # 현재 과제 시작 시간과 다음 과제 시작시간 간의 term

        # 진행 중 과제가 inturrupt 받지 않는 경우
        if time <= term:
            # 진행 중인 과제 완료 처리 (dummy data 예외 처리)
            if subject:
                answer.append(ing[2])

            # 다음 과제 시작까지 여유 시간이 있는 경우 멈춘 과제 진행
            extra_time = term - time

            while post_queue and extra_time > 0:
                last_time, subject = post_queue.popleft()

                if last_time > extra_time:
                    # 가장 최근에 멈춘 과제부터 수행되야 하므로 첫 번째 원소로 삽입
                    post_queue.appendleft([last_time - extra_time, subject])
                    break
                else:
                    extra_time -= last_time
                    answer.append(subject)

            # 새로운 과제 시작
            ing = heappop(subject_heap)

        # 진행 중 과제가 inturrupt 받는 경우
        else:
            time -= subject_heap[0][0] - start
            # 현재 과제 미루기
            # 가장 최근에 멈춘 과제부터 수행되야 하므로 첫 번째 원소로 삽입
            post_queue.appendleft([time, subject])
            # 새로운 과제 시작
            ing = heappop(subject_heap)

    # 현재 진행중인 과제 마무리
    answer.append(ing[2])

    # 멈춘 과제 순서대로 마무리
    while post_queue:
        answer.append(post_queue.popleft()[-1])

    return answer

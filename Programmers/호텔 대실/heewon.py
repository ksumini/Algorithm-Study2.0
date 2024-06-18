'''
[2024-06-18] heewon #97

## 함수 설명
- `timetomin`: 시간 문자열 (hh:mm 형식)을 분 단위 정수형으로 변환하는 함수입니다.

## 접근 방식
- 호텔 예약 정보를 대소 비교 가능한 분의 형태로 전환한다. 퇴실 시간은 10분 추가
- 호텔 예약 정보를 시작 시간을 기준으로 정렬한다.
- 차례대로 룸에 배정을 한다.
    - 룸에 들어오는 정보는 heap을 이용하여 퇴실 시간 기준으로 정렬한다.
    - 새로운 손님이 들어올 때
        - 대실 중이고 기존 손님의 퇴실 시간 <= 새로운 손님의 시작 시간이면
            - 기존 손님은 퇴실
        - 새로운 손님은 대실
        - 최대 대실 수 확인


## 사용한 모듈
`heapq`

## 추가 정보
- 시간: 20 min 이하
- 힌트: `None`
'''

import heapq

def solution(book_time:list)->int:
    """
    호텔 예약 정보를 바탕으로 최대 동시 예약 가능한 호텔 개수를 반환하는 함수입니다.

    Args:
        book_time: 호텔 예약 정보가 담긴 리스트입니다.
                    리스트의 각 요소는 시작 시간 (hh:mm 형식)과 종료 시간 (hh:mm 형식)을 
                    문자열 형태로 쌍 (tuple)으로 가지고 있습니다.
                    예) [("09:00", "10:30"), ("12:30", "14:30"), ...]

    Returns:
        최대 동시 예약 가능한 호텔 개수
    """

    answer = 0

    # 예약 시간을 분 단위 정수형으로 변환 (예: 09:00 -> 540), 퇴실을 10분 추가
    book_time = [[timetomin(st), timetomin(et) + 10] for st, et in book_time]
    # 예약 정보 시작 시간 기준으로 오름차순 정렬
    book_time.sort()

    # 최소 힙 (min-heap) 생성
    room = []
    for start, end in book_time:
        if room and start >= heap[0]:         # 대여 중이고 새로운 손님의 시작 시간 >= 기존 손님의 퇴실 시간
            earliest_end_time = heapq.heappop(room)     # 기존의 손님 퇴실
        else:
            answer += 1     # 방 추가 대여

        heapq.heappush(room, end)       # 현재 퇴실 시간을 힙에 추가

    return answer

def timetomin(time:str)->int:
    """
    시간 문자열 (hh:mm 형식)을 분 단위 정수형으로 변환하는 함수입니다.

    Args:
        time: 시간 문자열 (hh:mm 형식)

    Returns:
        분 단위 정수형 시간 (예: 09:00 -> 540)
    """

    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes

"""
<문제>
최소한의 객실 만을 사용해 예약 손님을 받는다.
한 번 사용한 객실은 '퇴실 시간'을 기준으로 10분 후 다음 손님이 사용 가능
-> 코니에게 필요한 최소 객실의 수를 반환

<제한 사항>
1 ≤ book_time의 길이 ≤ 1,000
- book_time[i]는 ["HH:MM", "HH:MM"]의 형태로 [대실 시작 시각, 대실 종료 시각]
- "00:00"부터 "23:59"까지로 주어진다.

<풀이 시간>
20분

<풀이>
1. 시작 시각을 기준으로 오름차순 정렬
2. 시각을 하나씩 확인하며 객실 배정
- 힙(종료시각)이 비어있다면 객실 추가
- 힙이 비어있지 않다면 힙에서 가장 빠른 종료 시각과 시작 시각을 비교
    - 시작 시각이 퇴실이 가장 빠른 객실의 종료 시각 + 10분 이후라면 해당 객실 사용 가능 -> heap에서 해당 객실의 종료시각 업데이트
    - 시작 시각이 퇴실이 가장 빠른 객실의 종료 시각 + 10분 이전이라면 새로운 객실 추가 배정 -> answer + 1

<시간 복잡도>
예약 시각 문자열 배열 정렬: O(NlogN)
각 예약에 대한 힙 연산: O(NlogK)
- K는 힙의 크기(최악의 경우, K는 N과 같을 수 있다. K<=N)
-> 전체 시간복잡도: O(NlogN)+O(NlogN)=O(NlogN)
"""
import heapq


def time_to_minutes(time_str: str):
    hh, mm = map(int, time_str.split(':'))
    return hh * 60 + mm


def solution(book_time: list) -> int:
    """
    :param book_time: 예약 시간이 문자열 형태로 담긴 2차원 배열
    :return: 코니에게 필요한 최소 객실의 수
    """
    answer = 0 # 코니에게 필요한 최소 객실의 수
    # 1. 시작 시각을 기준으로 오름차순 정렬
    book_time.sort(key=lambda x: x[0])
    heap = [] # 각 객실의 종료 시각이 담긴 최소힙
    # 2. 시각을 하나씩 확인하며 객실 배정
    for start, end in book_time:
        start_time = time_to_minutes(start)
        end_time = time_to_minutes(end) + 10

        # 힙이 비어있지 않으면(사용할 객실이 있음)서, 가장 빨리 퇴실하는 객실의 퇴실 시각 + 10분 이후에 입실하려고 한다면, 해당 객실을 사용(퇴실 시각 업데이트)
        if heap and start_time >= heap[0]:
            heapq.heappop(heap)
        else: # 힙이 비어있다면(이어서 사용할 객실이 없기 때문에) 새로운 객실 추가
            answer += 1

        heapq.heappush(heap, end_time)

    return answer


if __name__ == '__main__':
    print(solution(book_time=[["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])) # 3
    print(solution(book_time=[["09:10", "10:10"], ["10:20", "12:20"]])) # 1
    print(solution(book_time=[["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])) # 3
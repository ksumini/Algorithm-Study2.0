import sys
from collections import deque

def solution(n:int, lines:list, d:int):
    """
    n명. A-B 집, 사무실. 위치가 같을 수 있음. 통근하는 사람들 편의 위해 두 점을 잇는 철로를 건설. "집과 사무실 위치 모두 철"로 선분에 포함되는 사람들의 수가 최대로 되도록
    :param n: n 명
    :param lines: hi, oi  사람 i의 집과 사무실 위치
    :param d:  철로 길이
    :return:
    """
    events = []
    total = 0
    for i in range(n):
        events.append([min(lines[i]), 1]) # 선분을 쭉 피기 위함
        events.append([max(lines[i]), -1])
        if abs(lines[i][1] - lines[i][0]) <= d:
            total += 1

    if total <= 1: # 1개 이하면 바로 결과 추측 가능
        print(total)
        return None

    events.sort()
    events.append([10**10,1])  # 끝에 값 편하게 정리하기 위해
    #events.append([10**10+1,-1])

    start = events[0][0] # end = start+d
    max_overlap = 0
    candidate_overlap = 0
    q = deque(); q.append((start, 0)) # 구간 시작, 겹치는 수
    check_done_section = set()
    check_done_section.add(start)
    for i in range(1, 2*n+1):

        if events[i][1] == 1:
            candidate_overlap += 1
        else:
            candidate_overlap -= 1

        for _ in range(len(q)):
            start, overlap = q.popleft()

            if events[i][1] == 1: # 시작 부분
                if start+d > events[i][0]: # 영역안에 새로운 시작
                    q.append([start, overlap])
                else: # 영역 밖에서 시작임 start+d <= events[i][0]
                    #print("check start point : ", start, overlap)
                    max_overlap = max(max_overlap, overlap)
            else:  # 끝 부분
                if start + d >= events[i][0]:  # 끝나는 부분이 안에 있음
                    q.append([start, overlap+1])
                else:  # 끝나는 부분이 밖에 있음
                    #print("check start point : ", start, overlap)
                    max_overlap = max(max_overlap, overlap)

        if events[i][0] not in check_done_section and events[i][1] == 1:
            q.append([events[i][0], -candidate_overlap])
            check_done_section.add(events[i][0])

        #print(events[i], q)
    print(max_overlap)

    return None

if __name__ == "__main__":
    #sys.stdin = open("13334.txt")
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    d = int(input())
    solution(n, lines, d)





import sys
import heapq

# 한번 더 보기

def solution(n: int, lines: list, d: int):
    # 모든 선분을 집과 사무실의 위치로 정렬
    valid_lines = []
    for h, o in lines:
        start, end = min(h, o), max(h, o)
        if end - start <= d:  # 길이가 d 이하인 경우에만 고려
            valid_lines.append((start, end))

    if len(valid_lines) <= 1: # 1개 이하면 끝
        print(len(valid_lines))
        return None

    # 끝점을 기준으로 정렬
    valid_lines.sort(key=lambda x: x[1])

    max_count = 0
    current_heap = []

    for start, end in valid_lines:
        # 현재 힙에서 가장 시작점이 작은(=가장 멀리 떨어져있음) 애가 d거리 이상 차이남
        while current_heap and current_heap[0] < end - d:
            heapq.heappop(current_heap)

        # 현재 선분을 힙에 추가함
        heapq.heappush(current_heap, start)

        # 최대 인원 수 갱신
        max_count = max(max_count, len(current_heap))

    print(max_count)
    return None

if __name__ == "__main__":
    #sys.stdin = open("13334.txt")
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    d = int(input())
    solution(n, lines, d)
import heapq
import sys

# 실행 시간을 줄이기 위하여 필요
input = sys.stdin.readline

n = int(input())

locations = [list(map(int, input().split())) for _ in range(n)]

d = int(input())

# L이 가능한 경우만 고려
can_locations = [[min(a, b), max(a, b)] for a, b in locations if abs(b - a) <= d]

# 구간을 끝나는 점 기준으로 오름차순 정렬 (첫 번째 원소가 동일하면 두 번째 원소 기준으로 정렬)
can_locations.sort(key=lambda x: x[1])

# 힙을 사용해 구간 내에서 가장 많이 포함되는 구간 찾기
answer = 0
heap = []

for start, end in can_locations:
    heapq.heappush(heap, start)
    
    # 현재 구간의 끝에서 d를 넘어가는 구간들을 힙에서 제거
    while heap and heap[0] < end - d:
        heapq.heappop(heap)
    
    # 힙에 남아 있는 구간의 수가 포함된 구간의 수
    answer = max(answer, len(heap))

print(answer)
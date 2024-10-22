"""
<문제>
집과 사뭄실의 위치가 모두 d에 포함되는 사람들의 최대 수

<제한 사항>
n: 1 <= n <= 100,000
h, o: -100,000,000 이상 100,000,000 이하의 서로 다른 정수
d: 1 <= d <= 200,000,000

<풀이>
풀이 시간:
1. 각 사람의 집과 사무실 중 작은 값을 시작점으로 두고, 큰 값이 끝점이 되도록 정렬
2. 철로의 끝점을 기준으로 현재 집과 사무실 위치가 철로 길이 d 내에 모두 포함되는지 확인
3. 힙에 포함되지 않는 집 위치는 제거하고, 포함되는 집 위치는 힙에 추가하여 힙의 크기를 통해 최대 사람 수 업데이트

<시간 복잡도>
O(nlogn)
"""
import sys
import heapq

input = sys.stdin.readline

# 사람 수
n = int(input())
# h: 집, o: 사무실
places = []
for _ in range(n):
    h, o = map(int, input().split())
    # 집과 사무실 중 작은 값이 앞에 오도록 저장
    if h > o:
        h, o = o, h
    places.append([h, o])

# 철로의 길이
d = int(input())

# 끝점 기준으로 정렬
places.sort(key=lambda x: x[1])

# 우선순위 큐 (최소 힙)
heap = []
max_people = 0

# 슬라이딩 윈도우를 힙으로 관리
for start, end in places:
    # 철로의 끝점이 end이고, 시작점이 end - d 이상이어야 함
    # 즉, start가 end - d보다 작으면 철로에 포함되지 않으므로 제거
    while heap and heap[0] < end - d:
        heapq.heappop(heap)

    # 집과 사무실 모두 철로 구간에 포함되는지 확인하고 힙에 추가
    if end - d <= start:  # 집과 사무실이 모두 철로에 포함되는지 확인
        heapq.heappush(heap, start)

    # 현재 철로 구간에 포함되는 사람 수 갱신
    max_people = max(max_people, len(heap))

print(max_people)
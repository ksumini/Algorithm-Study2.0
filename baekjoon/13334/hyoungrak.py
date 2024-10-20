'''
- n명의 사람들
- 철로의 길이 d
- 집과 사무실의 위치 모두 철로 선분에 포함되는 사람들의 수가 최대
- windowing으로 해야하나?

1 <= n <= 100000
-100000000 <= hi, oi <= 100000000
1 <= d <= 200000000
'''
import heapq

n = int(input())

spots = []
for _ in range(n):
    hi, oi = map(int, input().split())
    spots.append([min(hi, oi), max(hi, oi)])
d = int(input())

spots.sort(key = lambda x: (x[1], x[0]))
heap = []
answer = 0

for spot in spots:
    if spot[1] - spot[0] <= d:          # d보다 작은 애들은 추가
        heapq.heappush(heap, spot[0])
    else:                   # 길이보다 큰 애들은 그냥 패쓰
        continue

    while heap:
        start = heap[0]

        if spot[1] - start > d:     # window크기보다 크면 탈락
            heapq.heappop(heap)
        else:
            break


    answer = max(len(heap), answer)

print(answer)

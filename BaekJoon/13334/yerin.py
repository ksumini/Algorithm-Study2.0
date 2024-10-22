import heapq

n = int(input())
home_office = []
for _ in range(n):
    h, o = map(int, input().split())
    home_office.append((min(h, o), max(h, o)))

d = int(input())

home_office.sort(key=lambda x: x[1])

max_count = 0
heap = []

for i in home_office:
    for end, start in (i[1], i[0]):
        while heap and heap[0] < end - d:
            heapq.heappop(heap)
        if start >= end - d:
            heapq.heappush(heap, start)
        max_count = max(max_count, len(heap))

print(max_count)

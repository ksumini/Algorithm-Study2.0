from collections import deque
import heapq
import sys


input = sys.stdin.readline
n, c = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(n)]
gems.sort()

info = []

total = 0
ans = 0

for w, h, v in gems:
    c -= 1
    total += v
    heapq.heappush(info, [-h, v])
    while c < 0:
        _, prev_v = heapq.heappop(info)
        c += 1
        total -= prev_v

    ans = max(ans, total)

print(ans)


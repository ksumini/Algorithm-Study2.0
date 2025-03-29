import sys
from collections import defaultdict
input = sys.stdin.readline
n, cash = map(int, input().split())

x_gems = defaultdict(list) # x좌표에 있는 보석들
y_gems = defaultdict(list) # y좌표에 있는 보석들

for _ in range(n):
    x, y, v = map(int, input().split())
    x_gems[x].append((y, v))
    y_gems[y].append((x, v))


result = 0
cost = 0 # 보석 채굴 비용 = 보석 갯수
value = 0
x = 100_000 # x좌표 최대값
y = 0 # y좌표 최소값


bag = set()

while x >= 0 and y <= 100_000:
    if cost <= cash: # 가방에 더 넣을수 있는 경우
        for _x, v in y_gems[y]:
            if _x <= x:
                bag.add((_x, y))
                cost += 1
                value += v
        y += 1
    else:
        for _y, v in x_gems[x]:
            if (x, _y) in bag: # 이미 가방에 있는 보석이라면
                bag.remove((x, _y))
                cost -= 1
                value -= v
        x -= 1

    if cost <= cash: # 파산하지 않는 경우
        result = max(result, value)

print(result)


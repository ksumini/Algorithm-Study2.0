from collections import defaultdict, deque, namedtuple

Point = namedtuple('Point', ['x', 'y'])
Mine = namedtuple('Mine', ['value', 'cost'])

n, cash = map(int, input().split())
minerals = defaultdict(lambda : defaultdict(int))


max_x = 0
max_y = 0

for _ in range(n):
    x, y, value = map(int, input().split())
    minerals[x][y] = value
    max_x = max(max_x, x)
    max_y = max(max_y, y)

mines = [[Mine(0,0) for _ in range(max_y+1)] for _ in range(max_x+1)]

q = deque()
q.append(Point(0,0))
result = 0

# BFS (?) 방식으로 탐색 -> 시간 초과
while q:
    point = q.popleft()
    x, y = point.x, point.y
    if x > max_x or y > max_y:
        continue

    # 이미 방문
    if mines[x][y].value != 0:
        continue

    value = mines[x-1][y].value + mines[x][y-1].value - mines[x-1][y-1].value + minerals[x][y]

    cost = mines[x-1][y].cost + mines[x][y-1].cost - mines[x-1][y-1].cost
    cost += 1 if minerals[x][y] > 0 else 0

    if cost > cash:
        value = -float("inf")

    mines[x][y] = Mine(value, cost)
    result = max(result, value)

    q.append(Point(x+1, y))
    q.append(Point(x, y+1))


print(result)
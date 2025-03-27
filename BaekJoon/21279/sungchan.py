from collections import defaultdict, deque, namedtuple

Mine = namedtuple('Mine', ['value', 'cost'])
MAX_X = MAX_Y = 100_000 + 1

minerals = defaultdict(lambda : defaultdict(int))

mines: defaultdict = defaultdict(lambda : defaultdict(lambda : Mine(0,0)))


point_x = {-1, MAX_X}
point_y = {-1, MAX_Y}

n, cash = map(int, input().split())
for _ in range(n):
    x, y, value = map(int, input().split())
    minerals[x][y] = value
    point_x.add(x)
    point_y.add(y)

point_x = sorted(point_x)
point_y = sorted(point_y)

max_value = 0

for x in point_x[1:]:
    y_value = 0
    y_cost = 0
    for y in point_y[1:]:
        y_value += minerals[x][y]
        y_cost += 1 if minerals[x][y] else 0
        value = mines[x - 1][y].value + y_value
        cost = mines[x - 1][y].cost + y_cost

        if cost > cash:
            value = float('-inf')
        else:
            max_value = max(max_value, value)
            # print(f"x: {x}, y: {y}, value: {value}, cost: {cost}")

        mines[x][y] = Mine(value, cost)





print(max_value)
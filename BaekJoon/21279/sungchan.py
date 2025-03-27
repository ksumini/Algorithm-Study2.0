from collections import defaultdict, deque, namedtuple
from dataclasses import dataclass

Point = namedtuple('Point', ['x', 'y'])

@dataclass
class Mine:
    value: int
    cost: int


n, cash = map(int, input().split())
minerals: dict[Point, int] = dict()
mines: dict[Point, Mine] = dict()

set_x = set()
set_y = set()

for _ in range(n):
    x, y, value = map(int, input().split())
    point = Point(x, y)
    minerals[point] = value
    set_x.add(x)
    set_y.add(y)


for x in set_x:
    for y in set_y:
        point = Point(x, y)
        mines[point] = Mine(0, 0)

for mineral_point, mineral_value in minerals.items():
    for mine_point in mines.keys():
        if mine_point.x < mineral_point.x and mineral_point.y < mine_point.y:
            continue

        if mineral_point.x <= mine_point.x or mineral_point.y <= mine_point.y:
            mines[mine_point].value += mineral_value
            mines[mine_point].cost += 1



max_value = 0
for mine in mines.values():
    if mine.cost <= cash:
        max_value = max(max_value, mine.value)

print(max_value)






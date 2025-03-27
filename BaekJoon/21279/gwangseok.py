import sys
input = sys.stdin.readline

N, C = map(int, input().split())

xs = []
ys = []
vs = []

x_pos = []
y_pos = []

for idx in range(N):
    x, y, v = map(int, input().split())
    xs.append((x, idx))
    ys.append((y, idx))
    vs.append(v)

    x_pos.append(x)
    y_pos.append(y)


xs.sort()
ys.sort()

cost = N
dig = [True] * N

min_x = 100_000
min_y = 100_000

while cost > C or (min_x != 0 and min_y != 0 and xs[-1][0] >= min_x and ys[-1][0] >= min_y):
    while dig[xs[-1][1]] is False:
        xs.pop()
    while dig[ys[-1][1]] is False:
        ys.pop()

    x, x_idx = xs[-1]
    y, y_idx = ys[-1]

    if vs[x_idx] >= vs[y_idx]:
        min_y, cur_idx = ys.pop()
        if dig[cur_idx]:
            min_x = x_pos[cur_idx]
            dig[cur_idx] = False
            cost -= 1
    else:
        min_x, cur_idx = xs.pop()
        if dig[cur_idx]:
            min_y = y_pos[cur_idx]
            dig[cur_idx] = False
            cost -= 1
        
answer = 0
for idx in range(N):
    if dig[idx]:
        answer += vs[idx]

print(answer)

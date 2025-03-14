d, n = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

# 더 얕은 깊이에서 더 작은 지름일 경우 피자를 넣을 수 없음
for i in range(1, d):
    if oven[i] > oven[i-1]:
        oven[i] = oven[i-1]

current_depth = d - 1
ans = 0
for p in pizza:
    while current_depth >= 0 and p > oven[current_depth]:
        current_depth -= 1
    if current_depth < 0:
        ans = 0
        break
    current_depth -= 1
    ans = current_depth + 2

print(ans)
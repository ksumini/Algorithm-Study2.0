import sys

input = sys.stdin.readline

N = int(input())
total = max_p = skip = 0
for _ in range(N):
    x, p = map(int, input().split())
    if total <= x:
        # 상금 제한을 초과하지 않는 경우
        total += p
        if p > max_p:
            max_p = p
    else:
        # 상금 제한을 초과하는 경우
        if skip == 2 or (skip and total - max_p > x):
            print('Zzz')
            sys.exit()
        if total - max_p > x:
            skip = 2
            continue
        skip = 1
        total += p
        if p > max_p:
            max_p = p
print('Kkeo-eok')

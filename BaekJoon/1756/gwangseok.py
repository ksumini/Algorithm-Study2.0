import sys
from collections import defaultdict
from bisect import bisect_left

input = sys.stdin.readline

D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

# 각 oven 크기 별 가장 작은 depth를 저장
# pizza 크기보다 작은 oven들 중 가장 작은 depth 위에 쌓아야 함.
oven_hash = defaultdict(lambda: 300001)
for idx, o in enumerate(oven): # O(D)
    oven_hash[o] = min(oven_hash[o], idx + 1)

oven_sorted = list(set(oven))
oven_sorted.sort()

# 현재 oven과 그것 보다 작은 oven들 중 가장 작은 depth를 저장
min_depth_among_not_pass_oven = {oven_sorted[0]: oven_hash[oven_sorted[0]]}
for idx in range(1, len(oven_sorted)):
    o = oven_sorted[idx]
    min_depth_among_not_pass_oven[o] = min(min_depth_among_not_pass_oven[oven_sorted[idx-1]], oven_hash[o])
    
cur_depth = D + 1
for p in pizza:
    idx = bisect_left(oven_sorted, p)
    
    if idx >= len(oven_sorted):
        # 전부 피자 크기보다 작음.
        cur_depth = 0
        break

    if idx == 0:
        # idx가 0이면 모든 oven이 피자보다 같거나 큼.
        # 단순히 하나 쌓음.
        cur_depth -= 1
        if cur_depth == 0:
            # oven보다 피자가 많은 경우...
            # 이 부분을 생각 못 해서 시간이 좀 걸렸다.
            break
    else:
        # idx가 0이 아니면, 본인 보다 작은 oven이 있음.
        # 작은 oven 크기들을 구해서 그것 바로 위에 있는 것을 찾아야함.
        # idx는 본인보다 크거나 같은 ovens 중 가장 작은 것. -> 불포함.
        oven_not_pass = oven_sorted[idx-1]
        
        if min_depth_among_not_pass_oven[oven_not_pass] < cur_depth:
            # cur_depth보다 작은 것이 있다면 그 위에 쌓음.
            cur_depth = min_depth_among_not_pass_oven[oven_not_pass] - 1
        else:
            # 현재 피자보다 작은 oven이 현재 depth 위에 없음.
            # 단순히 쌓음.
            cur_depth -= 1

        if cur_depth == 0:
            break

print(cur_depth)

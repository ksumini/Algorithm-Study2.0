import sys
input = sys.stdin.readline

N, G, K = map(int, input().split())
s, l, o = [0] * N, [0] * N, [0] * N

# 한 빵 당 최대 필요한 일: S_i=1, G=1e9, L_u=1e9 -> 1e9 + 1e9
max_day = int(2e9)

for i in range(N):
    s[i], l[i], o[i] = map(int, input().split())

    if o[i] == 0:
        max_day = min(max_day, G//s[i] + l[i])

# binary search로 G를 안 넘는 경과한 일수를 찾는다.
left = 0
right = max_day
ans = None
while left <= right:  # O(log_2 max_day) * O(NlogN)
    mid = (left + right) // 2

    # mid일 만큼 경과했을 때, 세균수
    each_g = [0] * N
    sum_g = 0

    for i in range(N): # O(N)
        each_g[i] = (s[i] * max(1, mid-l[i]), o[i])
        sum_g += each_g[i][0]

    # 최대한 적은 재료를 빼기 위해 greedy하게 뺀다.
    each_g.sort(reverse=True) # O(NlogN)
    if sum_g > G:
        if K > 0:
            k = K
            for v, r in each_g:
                if r == 1:
                    # 필요 없는 재료면 뺀다.
                    sum_g -= v
                    k -= 1
                    if sum_g <= G or k == 0:
                        break
            if sum_g > G: 
                # 세균수가 넘치면 일수를 줄인다.
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
        else: 
            right = mid - 1
    else: 
        ans = mid
        left = mid + 1

print(ans)

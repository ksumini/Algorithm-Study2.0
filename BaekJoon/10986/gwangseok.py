from collections import defaultdict

N, M = map(int, input().split())
nums = list(map(int, input().split()))

cum_num = [0] * N
value_j_dict = defaultdict(list)
for idx, num in enumerate(nums): # O(N)
    cum_num[idx] = (cum_num[idx-1] + num) % M
    value_j_dict[cum_num[idx]].append(idx)

ans = 0

for key, values in value_j_dict.items(): # O(M)
    k = len(values)
    ans += (k-1) * k // 2 # 0 + ... + k-1
    if key == 0: # 본인 포함
        ans += k

print(ans)

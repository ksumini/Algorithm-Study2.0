from bisect import bisect_left


N = int(input())
A = list(map(int, input().split()))

index = [[0, 0] for _ in range(N)]  # [부분 수열 길이, 숫자]
dp = [A[0]]
index[0] = [1, A[0]]
for i in range(1, N):  # NlogN / 이전 LIS 코드 로직과 동일
    num = A[i]
    if num > dp[-1]:
        dp.append(num)
        index[i] = [len(dp), num]
    else:
        target_index = bisect_left(dp, num)
        dp[target_index] = num
        index[i] = [target_index + 1, num]

sorted_index = sorted(index, reverse=True)  # NlogN / 내림차순 정렬
prev_index, prev_num = sorted_index[0]
ans = [prev_num for _ in range(prev_index)]

for i, num in sorted_index[1:]:  # N
    # 같은 인덱스를 가질 때(서로 다른 부분 수열에서 같은 위치에 있을 때),
    # 수가 클수록 부분 수열 길이가 길어질 수 있음
    if i == prev_index:
        continue
    # 더 작은 인덱스이고 수가 더 작은 경우, 갱신
    if i < prev_index and num < prev_num:
        prev_index = i
        prev_num = num
        ans[prev_index - 1] = num

print(len(ans))
print(*ans)
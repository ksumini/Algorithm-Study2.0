N, M = map(int, input().split())
A = list(map(int, input().split()))

rest = [0] * M
prefix_sum = 0
for i in range(N):
    prefix_sum += A[i]
    rest[prefix_sum % M] += 1

ans = rest[0]
for i in range(M):
    ans += rest[i] * (rest[i] - 1) // 2

print(ans)
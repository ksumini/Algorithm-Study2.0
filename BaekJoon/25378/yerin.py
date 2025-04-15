n = int(input())
rocks = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    dp[i] = max(dp[i], dp[i - 1] if i > 0 else 0)
    remaining = rocks[i]
    for j in range(i + 1, n):
        remaining = rocks[j] - remaining
        if remaining < 0:
            break
        if remaining == 0:
            dp[j] = max(dp[j], dp[i - 1] + 1 if i > 0 else 1)
            break

print(n - dp[n - 1])

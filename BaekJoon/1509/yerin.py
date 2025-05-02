s = input().strip()
n = len(s)

is_pal = [[False] * n for _ in range(n)]
dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(n):
    is_pal[i][i] = True

for i in range(n - 1):
    is_pal[i][i + 1] = (s[i] == s[i + 1])

for length in range(3, n + 1):
    for start in range(n - length + 1):
        end = start + length - 1
        is_pal[start][end] = (s[start] == s[end]) and is_pal[start + 1][end - 1]

for i in range(1, n + 1):
    for j in range(i):
        if is_pal[j][i - 1]:
            dp[i] = min(dp[i], dp[j] + 1)

print(dp[n])
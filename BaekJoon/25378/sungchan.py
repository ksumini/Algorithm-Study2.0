import sys
input = sys.stdin.readline

n = int(input())
rocks = list(map(int, input().split()))

dp = [0] * n
for i in range(n):
  dp[i] = max(dp[i],dp[i-1])
  pick = rocks[i]
  for j in range(i+1,n):
    pick = rocks[j]-pick
    if pick<0:
      break
    if pick==0: # 이전꺼랑 양이 같으면
      dp[j] = max(dp[j],dp[i-1]+1)
      break
#   print(i, dp)
print(n-dp[-1])
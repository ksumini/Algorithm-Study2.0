"""
<문제>
가장 긴 증가하는 부분 수열(LIS)를 구하라.

<제한 사항>
- 수열 A의 크기 N: (1 <= N <= 1,000,000)
- -1,000,000,000 ≤ Ai ≤ 1,000,000,000

<풀이>
풀이 시간: 1시간 40분
1. 각 원소에 대해 이진탐색을 통해 dp에 들어갈 위치를 찾는다.
2. 위치가 dp의 끝이면 추가하고, 아니면 기존값을 대체해 LIS 길이를 최적화한다.
3. last_idx와 parent를 업데이트해 각 값의 원래 위치와 연결 관계를 기록한다.
"""
from bisect import bisect_left


n = int(input())
a = list(map(int, input().split()))

dp = [] # LIS 저장 배열
parent = [-1] * n # 각 원소의 이전 원소 인덱스
last_idx = [-1] * (n+1) # LIS에서 마지막 원소의 인덱스 저장

for i, num in enumerate(a):
    pos = bisect_left(dp, num) # num이 들어갈 위치
    if pos == len(dp):
        dp.append(num) # LIS 배열에 새로 추가
    else:
        dp[pos] = num # LIS 배열 갱신

    last_idx[pos] = i # pos 위치의 원소 인덱스 저장

    if pos > 0:
        parent[i] = last_idx[pos - 1] # 이전 원소의 인덱스 저장

# 역추적해 LIS 복원
lis = []
temp = last_idx[len(dp) - 1] # 마지막 원소의 위치
while temp != -1:
    lis.append(a[temp])
    temp = parent[temp]

print(len(lis))
print(*lis[::-1])
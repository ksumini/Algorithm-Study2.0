"""
<풀이>
풀이 시간: 40분

1. prefix_sum[j] % m == premifx_sum[i] % m이면, 구간 [i, j]의 합은 m의 배수
-> 나머지가 같은 누적합을 가진 두 인덱스(i와 j)가 있으면, 구간 [i, j]의 합이 조건을 만족한다.

2. 나머지가 같은 누적합의 개수를 세고, 각 나머지에서 가능한 모든 쌍의 개수를 계산
- 나머지가 0인 경우는 [0, j] 구간도 포함하기 위해 1로 초기화

<시간복잡도>
O(n)
"""

from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 누적합과 나머지 계산
prefix_sum = 0
remainder_count = defaultdict(int)
remainder_count[0] = 1  # 초기값: 나머지가 0인 경우를 포함

for num in a:
    prefix_sum += num
    remainder = prefix_sum % m
    remainder_count[remainder] += 1

# 조합 계산
answer = 0
for count in remainder_count.values():
    if count > 1:
        answer += (count * (count - 1)) // 2

print(answer)
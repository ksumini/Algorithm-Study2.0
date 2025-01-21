"""
풀이 시간: 45분

<문제>
밀키트에 n개의 재료가 들어있다.
i번째 재료의 유통기한은 밀키트를 구매한 후 Li일까지이고, 부패 속도는 Si이다.
이 때, 구매 후 x일에 i번째 재료에 있는 세균 수는 Si x max(1, x - Li)마리

모든 재료의 세균수의 합이 G마리 이하일 경우, 안심하고 먹을 수 있다.
중요하지 않은 재료를 최대 K개까지 빼서 세균수가 G마리 이하라면 먹기로 했다.
산 날부터 며칠 후까지 먹을 수 있을까?

<풀이>
- 특정 날짜에 먹을 수 있는지 확인
- 이분 탐색으로 먹을 수 있는 최대 날짜 탐색

<시간 복잡도>
O(nlogn * log(10^9))
"""


import sys
input = sys.stdin.readline


n, g, k = map(int, input().split())

kits = [] # 밀키트 정보를 저장할 리스트
for i in range(n):
    # 부패속도, 유통기한, 중요한 재료 여부
    kits.append(list(map(int, input().split())))


def check(day):
    bacteria = [] # 중요하지 않은 재료들의 세균 수를 저장
    total = 0 # 반드시 사용해야 하는 재료들의 세균 수 합

    for s, l, o in kits:
        curr = s * max(1, day - l)  # 현재 세균 수 계산
        if o == 1: # 중요하지 않은 재료
            bacteria.append(curr)
        else: # 필수 재료
            total += curr

    # 중요하지 않은 재료 중 세균 수가 가장 많은 K개를 제외
    bacteria.sort(reverse=True)
    # k개를 제외하고 나머지는 더함
    for i in range(k, len(bacteria)):
        total += bacteria[i]

    return total <= g

left = 1
right = int(1e9) # 최대 가능한 날짜
answer = 0

while left <= right:
    mid = (left + right) // 2
    if check(mid): # mid일째에 먹을 수 있다면
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
from collections import namedtuple
from sys import stdin

Contest = namedtuple("Contest", ["limit", "prize"])
N = int(stdin.readline())

contests = [
    Contest(*map(int, stdin.readline().split()))
    for _ in range(N)
]

result = "Kkeo-eok"
total_prize = 0
max_prize = 0
skip_prize = 0
skip = False

for limit, prize in contests:
    if total_prize - skip_prize > limit: # 넘어간 상금 기준으로 계산
        if skip: # 불참한 적이 이미 있으면 실패
            result = "Zzz"
            break

        skip = True
        if max_prize > prize and total_prize - max_prize <= limit: # 이전 대회 불참
            skip_prize = max_prize
        else: # 이번 대회를 불참
            skip_prize = prize

    total_prize += prize # 총 상금은 스킵 여부 따지지 않고 더함
    max_prize = max(max_prize, prize)

print(result)


# DP = [ [0] * 2 for _ in range(N+1)]
# for i in range(N):
#     if DP[i][0] != FAIL and DP[i][0] <= contests[i].limit:
#         DP[i+1][0] = DP[i][0] + contests[i].prize # 이번 경기 참가
#         DP[i + 1][1] = DP[i][0] #  이번 경기 안참가
#
#     elif DP[i][1] != FAIL and  DP[i][1]<= contests[i].limit:
#         DP[i+1][0] = DP[i][1] + contests[i].prize
#         DP[i + 1][1] = FAIL
#         count += 1
#     else:
#         result = "Zzz"
#         break
#     if count > 1:
#         result = "Zzz"
#         break
"""
mid ~ 2, 3, 4m

탑승한 사람 무게 == 시소 축 * 좌석 간의 거리

return 시소 짝꿍 몇쌍
- 100 -> 200, 300, 400 / 200, 300, 400
- 180 -> 360, 540, 720
- 360 -> 720, 1080, 1440
- 270 -> 540, 810, 1080

{200, 300, 400, 360, 540, 720, 1080, 1440, 810, 940}
-> {100, 100}, 720, 540, 1080
"""

from collections import defaultdict
from itertools import combinations


def solution(weights):
    answer = 0
    distances = [2, 3, 4]  # 거리 배열
    values = defaultdict(list)  # 토크 크기 : [무게]
    weight_cnt = defaultdict(int)  # 무게 별 개수 딕셔너리

    for weight in weights:
        if weight not in weight_cnt:  # 같은 무게 중복 탐색 제외
            for dist in distances:
                values[weight * dist].append(weight)
        weight_cnt[weight] += 1

    # 동일한 무게가 1개보다 많은 경우. 조합 계산 (a == b의 경우)
    for v in weight_cnt.values():
        if v > 1:
            answer += v * (v-1) // 2

    # (a != b의 경우) 조합 계산
    for k, v in values.items():
        for a, b in combinations(v, 2):
            answer += weight_cnt[a] * weight_cnt[b]

    return answer

# print(solution([100,180,360,100,270]))
# print(solution([2,2]))
# print(solution([3, 7, 100]))
# print(solution([180, 360, 270]))
# print(solution([1, 1, 2]))
print(solution([2, 3, 4, 6, 8]))
print("----------")
print(solution([2, 2, 2]))
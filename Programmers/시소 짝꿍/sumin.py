"""
<문제>
탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면 시소 짝꿍이라고 한다.
사람들의 몸무게 목록이 주어질 때, 시소 짝꿍이 몇 쌍 존재하는지 구하라.

<제한 사항>
- 2 ≤ weights의 길이 ≤ 100,000
- 100 ≤ weights[i] ≤ 1,000

<풀이 시간>
45분

<풀이>
1. 가능한 거리 조합 및 비율
- (1, 1) -> 1
- (2, 3) -> 3/2
- (2, 4) -> 4/2 = 2
- (3, 4) -> 4/3
- (3, 2) -> 2/3
- (4, 2) -> 2/4
- (4, 3) -> 2/4

2. 딕셔너리를 통해 빈도수 계산
- 몸무게의 비율을 계산한 후, 각 몸무게가 해당 비율에 맞는 다른 몸무게와 짝이될 수 있는지 확인
- 비율에 맞는 다른 몸무게가 있다면, 그 개수를 answer에 더하기

<시간 복잡도>
1. 몸무게 순회: O(n)
2. 비율 계산 및 검색: 7개의 가능한 비율을 계산하기 때문에, 상수시간: O(1)
-> O(n)
"""
from collections import defaultdict


def solution(weights: list) -> int:
    answer = 0 # 시소 짝꿍 쌍
    # 1. 각 몸무게의 빈도를 저장할 딕셔너리
    weights_cnt = defaultdict(int)
    # 2. 몸무게 순회
    for weight in weights:
        # 각 거리 조합에 대한 비율 계산 및 짝 찾기
        possible_pairs = [weight, weight * (3/2), weight * 2, weight * (4/3), weight * (2/3), weight * (1/2), weight * (3/4)]
        for pair in possible_pairs:
            if pair in weights_cnt:
                answer += weights_cnt[pair]
        weights_cnt[weight] += 1

    return answer
from collections import Counter


def solution(weights: list) -> int:
    answer = 0
    weights = Counter(weights)

    # (a==b) / (a*2 == b*3) / (a*2 == b*4) / (a*3 == b*4)
    for k, v in weights.items():
        # print(k, v)
        if v >= 2:  # 같은 경우
            answer += v * (v - 1) / 2

        if k * 2 / 3 in weights:
            answer += v * (weights[k * 2 / 3]) / 2
        if k * 3 / 2 in weights:
            answer += v * (weights[k * 3 / 2]) / 2
        if k * 2 / 4 in weights:
            answer += v * (weights[k * 2 / 4]) / 2
        if k * 4 / 2 in weights:
            answer += v * (weights[k * 4 / 2]) / 2
        if k * 3 / 4 in weights:
            answer += v * (weights[k * 3 / 4]) / 2
        if k * 4 / 3 in weights:
            answer += v * (weights[k * 4 / 3]) / 2

    return answer
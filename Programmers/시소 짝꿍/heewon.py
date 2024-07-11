from collections import Counter

def solution(weights):
    """
    주어진 무게 리스트 `weights` 에서 가능한 모든 쌍의 합이 동일한 쌍을 찾아 그 개수를 반환하는 함수입니다.

    Args:
        weights: 각 원소가 무게 값을 나타내는 리스트입니다.

    Returns:
        가능한 모든 쌍의 합이 동일한 쌍의 개수입니다.
    """
    answer = 0
    wc = Counter(weights)   # weight : 개수
    for w in wc.keys():     # 각 weight에 대해 탐색
        for ratio in [1/2, 2/3, 3/4, 1]:
            if w * ratio in wc:  # 쌍이 weights에 포함되는지 검사
                if ratio == 1:  # 동일 위치에 있는 경우 (w와 w * ratio 값이 동일)
                    # 조합을 이용 (nC2 = n * (n-1) / 2)
                    answer += wc[w] * (wc[w] - 1) / 2
                else:   # 다른 위치에 있는 경우 (w와 w * ratio 값이 다른 경우)
                    answer += wc[w] * wc[w * ratio]     # w의 개수 * w의 쌍 개수

    return answer
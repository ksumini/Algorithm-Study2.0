from collections import defaultdict


def solution(target):
    """
    DP로 풀었다. Dict 자료형으로 풀었음
    :param target:
    :return:
    """
    NUM_DICT = defaultdict(lambda: [10 ** 6, 10 ** 6])  # [target] = result
    # single or bool
    for i in range(1, 21):
        NUM_DICT[i] = [1, 1]
    NUM_DICT[50] = [1, 1]

    # double
    for i in range(22, 42, 2):
        NUM_DICT[i] = [1, 0]
    # triple
    for i in range(21, 63, 3):
        NUM_DICT[i] = [1, 0]

    if target in NUM_DICT:
        return NUM_DICT[target]

    for i in range(23, target + 1):
        candidates = []
        candidates.append([NUM_DICT[i - 50][0] + 1, NUM_DICT[i - 50][1] + 1]) # 현재점수-50에서 50점 1발 맞췄을 때
        candidates.append([NUM_DICT[i - 60][0] + 1, NUM_DICT[i - 60][1]]) # 현재점수-60에서 60점 1발 맞췄을 때
        candidates.append([NUM_DICT[i - 20][0] + 1, NUM_DICT[i - 20][1] + 1])  # 현재점수-20에서 20점 1발 맞췄을 때
        candidates.append(NUM_DICT[i])

        candidates.sort(key=lambda x: (x[0], -x[1]))
        NUM_DICT[i] = candidates[0]

    return NUM_DICT[target]
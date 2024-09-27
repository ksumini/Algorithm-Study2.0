from collections import defaultdict


def cal_n_comb_2(num):
    return num * (num - 1) // 2


def solution(weights):
    answer = 0
    weight_num = defaultdict(int)
    
    for weight in weights:
        weight_num[weight] += 1
    
    candidates = defaultdict(list)
    for weight, num in weight_num.items():
        if num >= 2:
            # 같은 숫자를 가지는 것들의 개수를 구한다.
            # nC2로 조합 수를 구한다.
            # 서로 같은 수 * 2, * 3, * 4는 계속 같기 때문에 이를 먼저 계산한다.
            answer += cal_n_comb_2(num)
        
        for mul_num in [2, 3, 4]:
            # weight에서 2, 3, 4를 곱했을 때 가능한 수를 미리 구한다.
            # 서로 다른 weight에 대한 number를 곱하므로, list의 최대 크기는 3이다.
            candidates[mul_num * weight].append(num)
    
        
    for k, vs in candidates.items():
        # 길이가 1일 때는 본인 자신만 있고, 다른 수와 짝이 이뤄지지 않는 것이다.
        # 길이가 2, 3일 때 가능한 경우의 수는 각 수들을 각각 곱한 것(순열)의 합이다.
        if len(vs) == 2:
            answer += vs[0] * vs[1]
        
        if len(vs) == 3:
            answer += vs[0] * vs[1]
            answer += vs[1] * vs[2]
            answer += vs[2] * vs[0]
    
    return answer

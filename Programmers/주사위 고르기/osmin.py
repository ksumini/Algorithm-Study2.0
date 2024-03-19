from itertools import combinations, product
from collections import Counter

def solution(dice):
    def choose_(dice): # 주사위 고르는 함수
        # input: 전체 주사위
        # output: 선정된 주사위, 선정되지 않은 주사위
        dice_idx = list(range(1, len(dice) + 1))
        selected = list(combinations(dice_idx,len(dice)//2))
        ls = len(selected) // 2
        return selected[:ls], list(reversed(selected[ls:]))

    def sum_(dice_idxs): # 주사위 합계 계산하는 함수
        # input: 선택된 주사위들(index)
        # output: 가능한 합계의 경우의 수
        return Counter(map(sum,product(*[dice[i-1] for i in dice_idxs])))
    
    def compare_dices_sum(dice1, dice2): # 주사위 결과 비교하는 함수
        # input: 주사위 두 개
        # output: 두 주사위의 전적(승, 무, 패)
        win, draw, loss = 0, 0, 0
        result1, result2 = sum_(dice1), sum_(dice2)
        for r1, r2 in product(result1, result2):
            # list로 나이브하게 계산시 시간 초과
            cases = result1[r1] * result2[r2]
            if r1 > r2:
                win += cases
            elif r1 < r2:
                loss += cases
            else:
                draw += cases
        return [win, draw, loss]
        
    result = []
    slct_dices, unslct_dices = choose_(dice)
    for slct, unslct in zip(slct_dices, unslct_dices):
        result.append([compare_dices_sum(slct, unslct),slct, unslct])
    result.sort(key=lambda x:max(x[0][0],x[0][2]), reverse=True)
    outcome, dset1, dset2 = result[0]
    answer = dset1 if outcome[0] > outcome[2] else dset2
    
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/258709
# 1 hour

from collections import defaultdict
from itertools import combinations

def solution(dice):
    answer = []
    # 승률이 가장 좋은 경우 확인용 변수
    max_win = 0
    
    # 조합으로 구하는 주사위 쌍 구하기
    dice_case = list(combinations(range(len(dice)), len(dice)//2))
    dice_set = [[dice_case[i], dice_case[-1-i]] for i in range(len(dice_case)//2)]

    for a, b in dice_set:
        # A, B의 주사위 합의 경우 딕셔너리로 저장
        case_a = defaultdict(int)
        case_b = defaultdict(int)

        # A의 주사위 합의 빈도수 구하기
        for dice_num in a:
            c_a = defaultdict(int)
            # 1st dice
            if not case_a:
                for num in dice[dice_num]:
                    case_a[num] += 1
            # 이전의 합 빈도수에 새로운 주사위의 합 빈도수 구하기
            else:
                for before_case in case_a.keys():
                    for num in dice[dice_num]:
                        c_a[before_case+num] += case_a[before_case]
                case_a = c_a
        
        # B의 주사위 합의 경우 구하기
        for dice_num in b:
            c_b = defaultdict(int)
            # 1st dice
            if not case_b:
                for num in dice[dice_num]:
                    case_b[num] += 1
            # 이전의 합 빈도수에 새로운 주사위의 합 빈도수 구하기
            else:
                for before_case in case_b.keys():
                    for num in dice[dice_num]:
                        c_b[before_case+num] += case_b[before_case]
                case_b = c_b

        # A, B의 승패 구하기 
        win, draw, loss = 0, 0, 0
        for aa in case_a.keys():
            for bb in case_b.keys():
                if aa > bb:
                    win += case_a[aa] * case_b[bb]
                elif aa == bb:
                    draw += case_a[aa] * case_b[bb]
                else:
                    loss += case_a[aa] * case_b[bb]

        # 최고의 승률은 주사위 번호 저장
        if max_win < win:
            max_win = win
            answer = [x + 1 for x in a]
        if max_win < loss:
            max_win = loss
            answer = [x + 1 for x in b]

    return answer
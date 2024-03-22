from itertools import combinations
def solution(coin, cards):    
    def initialize(cards): # 카드 뭉치에서 손으로 1/3을 가져오는 함수
        return cards[:len(cards) // 3], cards[len(cards) // 3:]
    
    def pick_(cards, hand): # 카드 뭉치에서 손으로 카드 두 장을 가져오는 함수 
        if cards: # 카드 뭉치에 카드가 있다면
            hand.extend(cards[:2])
            return hand, cards[2:] # 손에 든 카드, 카드 뭉치
        return [], [] # 카드 뭉치에 카드가 없는 경우
    
    def submit_candidate(hand): # 제출 가능한 카드 조합을 계산하는 함수
        return [c for c in list(combinations(hand,2)) if sum(c) == n + 1]
    
    def submit_from_(hand, cand): # 손에서 카드 두 장을 제출하는 함수
        # return list(set(hand) - set(cand)) # set 차집합 연산 도중 순서가 바뀌어 오답 출력. 1시간 소요.
        return [h for h in hand if h not in cand]
            
    # 제출 가능한 카드 조합이 여러 개가 발생하기 때문에 분기점 발생, dfs 필요하다고 판단함.
    def dfs(hand, cards, round_, coin): 
        nonlocal round_max, n, picked
        round_ += 1
        hand, cards = pick_(cards, hand)
        picked |= set(hand[-2:]) # 방금 뽑은 카드 picked에 추가
        # print(n + 1, hand, cards, round_, picked, coin)
        if round_max < round_:
            round_max = round_

        if not hand: # 카드 뭉치가 없는 경우 리턴.
            return round_max

        for cand in submit_candidate(hand): # 가능한 제출 조합 모두를 dfs로 탐색
            # 뭉치에서 가져올 때 코인을 사용하지 않고, 해당 카드를 picked로 추적하다가 제출할 때 코인을 사용.
            used_coin = len((set(cand) & picked))
            if coin < used_coin:
                continue
            picked -= set(cand) # picked에서 제출한 카드 제거
            hand = submit_from_(hand, cand) # hand에서 제출한 카드 제거
            
            round_max = max(round_max, dfs(hand, cards, round_, coin - used_coin))
            
            hand = hand[:2] # hand 복구
            picked |= set(cand) # picked 복구
        return round_max
    
    round_max = 0
    picked, n = set(), len(cards)
    hand, cards = initialize(cards)
    round_max = dfs(hand, cards, 0, coin)
    return round_max

'''
1~n 수 적힌 카드 뭉치 n개, 중복 없고 순서 무작위.
동전 coin 개

시작
동전은 카드와 교환 가능
카드 1/3 뽑아서 손에 가지기

종료
카드 뭉치에 카드가 없으면
# 카드 뭉치에 카드가 한 장만 남는 경우는 없음. 2의 배수.
라운드 끝날 때 손에서 카드를 못 내면
마지막 라운드는 해당 라운드도 포함됨. 즉, 최소 1라운드는 진행됨.

라운드마다
카드 두 장 뽑기
한 장당 동전 하나로 가지거나, 버리기
카드에 적힌 수 합이 n + 1이 되도록 카드 두 장을 내야 함.


return: 최대로 도달 가능한 라운드 수

알고리즘: 단순 구현 문제
시간 복잡도: 카드 1000개
관건# 
카드는 최상단에서만 뽑을 수 있나? yes


구현 사항
손에 카드 추가하기(initialize)
라운드 진행하기
1. 카드 두 장 뽑기
2. 뽑은 카드 중 동전으로 선택하기
3. 두 카드 합이 n + 1이 되도록 내기
    카드 제출 가능한지 확인하는 함수

    
def submit_card_from_(hand): # 손에서 낼 수 있는 카드 경우의 수가 여러 개인 경우 분기점 발생. dfs 필요.
    # list(map(sum,combinations(hand,2))) # 단순 합으로 최적해 계산 불가.
    return out, hand

'''

'''
코인이 1개일 때 어떤 코인을 가져가느냐에 따라 분기점 발생.
코인은 카드를 사용할 때 감소되는 것으로 하자.
하지만 어차피 다음턴에 카드 부족으로 종료. -> 그렇지는 않음.
'''
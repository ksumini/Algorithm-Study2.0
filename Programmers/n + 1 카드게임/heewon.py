'''
## 변수 설명
- `answer`: 라운드
- `n`: 총 카드의 수
- `first_cards`: 처음에 받은 카드들
- `keep_cards`: coin을 사용하기 전의 대기 중인 카드들
- `cards`: 카드 뭉치에 남은 카드들
- `life`: 현재의 n + 1을 낼 수 있는 횟수

## 접근 방식
- DFS로 접근 -> 시간 초과
- coin을 꼭 사용해야 하는 상황에 사용하기
    - 내가 처음에 받은 카드와 쌍을 이루면 coin을 1개 사용
    - life가 없다면 `keep_cards`에서 쌍을 찾아서 coin 2개 이용

## 사용한 모듈
`없음`

## 추가 정보
- 시간: 4 hour
- 힌트: 아이디어만 확인

#19 [n + 1](https://school.programmers.co.kr/learn/courses/30/lessons/258707#)
'''

def solution(coin, cards):
    answer = 1
    # 전체 카드 수
    n = len(cards)

    # 플레이어가 처음 시작하는 카드
    first_cards = []
    life = 0

    # first_cards 구하기
    for i in range(n // 3):
        # 현재 카드의 쌍이 플레이어의 카드에 있는지 확인
        if n + 1 - cards[i] in first_cards:
            # 쌍이 발견되면 라이프를 증가하고 카드를 제거
            life += 1
            first_cards.remove(n + 1 - cards[i])
        else:
            # 쌍이 없으면 플레이어의 카드에 현재 카드 추가
            first_cards.append(cards[i])

    # 덱에서 first_cards 제거
    cards = cards[n // 3:]

    # Keep할 카드들
    keep_cards = []

    # 모든 카드가 소진될 때까지 게임 진행
    while(len(cards)):
        # 덱에서 두 개의 카드 선택
        card_one, card_two = cards[0], cards[1]

        # 첫 번째 선택한 카드의 쌍이 플레이어의 카드에 있는지 및 플레이어가 코인을 가지고 있는지 확인
        if n + 1 - card_one in first_cards and coin > 0:
            # 라이프를 증가하고 코인 개수를 감소
            life += 1
            coin -= 1
        else:
            # 첫 번째 선택한 카드를 플레이어의 손에 남은 카드 리스트에 추가
            keep_cards.append(card_one)
        
        # 두 번째 선택한 카드의 쌍이 플레이어의 카드에 있는지 및 플레이어가 코인을 가지고 있는지 확인
        if n + 1 - card_two in first_cards and coin > 0:
            # 라이프를 증가하고 코인 개수를 감소
            life += 1
            coin -= 1
        else:
            # 두 번째 선택한 카드를 플레이어의 손에 남은 카드 리스트에 추가
            keep_cards.append(card_two)
        
        # 현재 라이프와 남은 코인 수를 기준으로 게임을 계속할지 여부 확인
        if life == 0:
            if coin < 2:
                break
            for keep_card in keep_cards:
                if n + 1 - keep_card in keep_cards:
                    life += 1
                    coin -= 2
                    keep_cards.remove(n + 1 - keep_card)
                    keep_cards.remove(keep_card)
                    break
            else:
                break
        
        # 각 라운드가 끝난 후 라이프 감소, 덱에서 선택한 카드 제거 및 총 라운드 수 증가
        life -= 1
        cards = cards[2:]
        answer += 1
    
    # 총 라운드 수 반환
    return answer


# DFS 시도 -> 시간 초과

from collections import defaultdict

def solution(coin, cards):
    answer = 0
    n = len(cards)
    my_card = defaultdict(int)
    round_cnt = 0
    for i in range(0, n//3):
        if my_card[n+1-cards[i]] == 1:
            round_cnt += 1
            my_card[cards[i]] = -1
            my_card[n+1-cards[i]] = -1
        else:
            my_card[cards[i]] = 1
    # print(round_cnt, my_card)
    cards = cards[n//3:]
    # print(cards)
    answer = dfs(n, round_cnt, my_card, coin, cards)
    return answer
        
def check(n, round_cnt, my_card, get_card):
    rc = round_cnt
    mc = my_card.copy()
    for card in get_card:
        if mc[n+1-card] == 1:
            rc += 1
            mc[card] = -1
            mc[n+1-card] = -1
        else:
            mc[card] = 1
    # print(rc, mc)
    return rc, mc

def dfs(n, round_cnt, my_card, coin, cards):
    # print(n, round_cnt, my_card, coin, cards)
    depth = 1
    dep_list = [0]
    if len(cards) == 0:
        return 1
    if coin >= 2:
        rc, mc = check(n, round_cnt, my_card, cards[0:2])
        if rc > 0:
            dep_list.append(dfs(n, rc - 1, mc, coin - 2, cards[2:]))
        # if coin < len(cards):
        rc, mc = check(n, round_cnt, my_card, [cards[0]])
        if rc > 0:
            dep_list.append(dfs(n, rc - 1, mc, coin - 1, cards[2:]))
        rc, mc = check(n, round_cnt, my_card, [cards[1]])
        if rc > 0:
            dep_list.append(dfs(n, rc - 1, mc, coin - 1, cards[2:]))
        if round_cnt > 0:
            dep_list.append(dfs(n, round_cnt - 1, my_card, coin, cards[2:]))
    elif coin == 1:
        rc, mc = check(n, round_cnt, my_card, [cards[0]])
        if rc > 0:
            dep_list.append(dfs(n, rc - 1, mc, coin - 1, cards[2:]))
        rc, mc = check(n, round_cnt, my_card, [cards[1]])
        if rc > 0:
            dep_list.append(dfs(n, rc - 1, mc, coin - 1, cards[2:]))
        if round_cnt > 0:
            dep_list.append(dfs(n, round_cnt - 1, my_card, coin, cards[2:]))
    else:
        if round_cnt > 0:
            dep_list.append(dfs(n, round_cnt - 1, my_card, coin, cards[2:]))
    # print(dep_list)
    return depth + max(dep_list)


print(solution(4,	[3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))
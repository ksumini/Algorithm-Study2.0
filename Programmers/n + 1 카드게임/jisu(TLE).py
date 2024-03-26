"""
- 접근 1: 백트래킹을 활용한 접근(TLE)
    - 라운드, 카드 순서대로 탐색하여 각 라운드 별 아래 4개의 분기로 재귀한다.
        - 카드 1, 2를 모두 가져가는 경우
        - 카드 1만 가져가는 경우
        - 카드 2만 가져가는 경우
        - 카드를 모두 안가져가는 경우
    - 재귀가 최대 2^1000번 이상 일어나므로 TLE
"""
from typing import List, Tuple


def get_target(cards: List[int], target: int) -> Tuple[int, int]:
    """
    :param cards: 현재 라운드까지 드로우한 카드
    :param target: n+1
    :return: 두 카드 쌍의 인덱스 반환

    정렬 후 투포인터를 활용해 target(n+1)을 만들 수 있는 두 카드쌍의 인덱스를 반환한다.
    """
    cards.sort()
    i, j = 0, len(cards)-1

    while i < j:
        tmp_sum = cards[i]+cards[j]

        if tmp_sum < target:
            i += 1
        elif tmp_sum > target:
            j -= 1
        else:
            return i, j

    return -1, -1


def solution(coin: int, cards: List[int]) -> int:
    n = len(cards)
    target = n+1
    result = 0

    # 초기 드로우 카드
    draw_cards = [cards[i] for i in range(n//3)]

    def recur(draw_cards: List[int], left_coin, k) -> None:
        nonlocal result

        if k > result:
            result = k

        if k > n//3:
            # 최대 라운드 진출 시 재귀 종료
            return

        # 추가 카드
        card1, card2 = cards[(n//3)+2*(k-1)], cards[(n//3)+2*(k-1)+1]   # 각 라운드(k) 별로 뽑는 카드는 정해져있음

        # 카드 두 개 가져가는 경우
        if left_coin >= 2:
            nxt_cards = draw_cards + [card1, card2]
            i, j = get_target(nxt_cards, target)
            # target을 만들 수 있으면 재귀
            if i != -1:
                nxt_cards.pop(i)
                nxt_cards.pop(j-1)
                recur(nxt_cards, left_coin-2, k+1)

        # 카드를 한 개 가져가는 경우
        if left_coin >= 1:
            nxt_cards = draw_cards + [card1]
            i, j = get_target(nxt_cards, target)
            # target을 만들 수 있으면 재귀
            if i != -1:
                nxt_cards.pop(i)
                nxt_cards.pop(j-1)
                recur(nxt_cards, left_coin-1, k+1)

            nxt_cards = draw_cards + [card2]
            i, j = get_target(nxt_cards, target)
            # target을 만들 수 있으면 재귀
            if i != -1:
                nxt_cards.pop(i)
                nxt_cards.pop(j-1)
                recur(nxt_cards, left_coin-1, k+1)

        i, j = get_target(draw_cards, target)
        # target을 만들 수 있으면 재귀
        if i != -1:
            draw_cards.pop(i)
            draw_cards.pop(j-1)
            recur(draw_cards, left_coin, k + 1)

    recur(draw_cards, coin, 1)

    return result

def main():
    case1 = [4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]]
    case2 = [3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]]
    case3 = [2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]]
    case4 = [10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]

    print(solution(*case1))     # 5
    print(solution(*case2))     # 2
    print(solution(*case3))     # 4
    print(solution(*case4))     # 1

main()
"""
- 접근 2: 로직을 활용한 풀이
  - [ref1](https://school.programmers.co.kr/questions/72868),
  - [ref2](https://jaimemin.tistory.com/2350)

- key : 1~n 까지의 수 중 n+1을 만드는데 각 수는 최대 한 번 사용된다. ([1, n], [2, n-2], ...)
    - 이는 즉, 각 라운드마다 어떤 카드를 내던지 n+1을 만들기만 하면 된다는 것을 의미한다.
      - 각 라운드마다 어떤 카드 쌍으로 n+1을 만들지 생각 안해도 된다는 얘기
- 따라서, 뽑은 카드를 안가져오고도 n+1을 만들 수 있으면 만들되, 만들 수 없으면 지금까지 뽑았던 수를 가져와서 만들면 된다.
    - 1. 현재 카드만으로 n+1 만들기 (코인 0 소모)
    - 2. 현재 카드 1 + 뽑은 카드 1 로 n+1 만들기 (코인 1 소모)
    - 3. 뽑은 카드 2 로 n+1 만들기 (코인 2 소모)
- (핵심) 우선 모두 무료로 가져온 뒤, 보유한 카드를 제출 할 때 후불 감당 가능하면 다음 라운드로 진출하면 된다.
"""
from collections import deque
from typing import List, Set


def judge(origin: Set[int], other: Set[int], target: int):
    """
    두 카드 뭉치로 target(n+1)을 만들 수 있으면 해당 원소 제거 후 True를 반환한다.
    만들 수 없다면 False를 반환한다.

    :param origin:  비교 카드뭉치 1
    :param other: 비교 카드뭉치 2
    :param target: n+1
    :return: target을 만들 수 있는지 여부
    """
    for card in origin:
        other_card = target-card

        if other_card in other:
            origin.remove(card)
            other.remove(other_card)
            return True

    return False


def solution(coin: int, cards: List[int]) -> int:
    n = max(cards)
    target = n+1
    cards = deque(cards)
    answer = 1

    # hand: 가져온 카드, draw: 뽑은 카드
    hand, draw = set(), set()
    # 초기 드로우
    for _ in range(n//3):
        hand.add(cards.popleft())

    while cards:
        # 매 턴 2장 드로우
        for _ in range(2):
            draw.add(cards.popleft())

        # 현재 카드만으로 n+1 만들기 (코인 0 소모)
        if len(hand) >= 2 and judge(hand, hand, target):
            answer += 1
        # 현재 카드 1 + 뽑은 카드 1 로 n+1 만들기 (코인 1 소모)
        elif len(hand) >= 1 and coin >= 1 and judge(hand, draw, target):
            answer += 1
            coin -= 1
        # 뽑은 카드 2 로 n+1 만들기 (코인 2 소모)
        elif coin >= 2 and judge(draw, draw, target):
            answer += 1
            coin -= 2
        # 만들 수 없는 경우 종료
        else:
            break

    return answer


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
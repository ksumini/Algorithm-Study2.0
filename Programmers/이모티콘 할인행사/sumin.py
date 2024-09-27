"""
<문제>
1. 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것
2. 이모티콘 판매액을 최대한 늘리는 것
-> 우선순위: 1번 목표 > 2번 목표

- n명의 카카오톡 사용자들에게 이모티콘 m개를 할인하여 판매한다.
- 이모티콘마다 할인율은 다를 수 있으며, 할인율은 10%, 20%, 30%, 40% 중 하나로 설정된다.
- 각 사용자들은 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매한다.
- 각 사용자들은 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입한다.

<제한 사항>
- 1 ≤ users의 길이 = n ≤ 100
    - users의 원소는 [비율, 가격]의 형태
    - users[i]는 i+1번 고객의 구매 기준
    - 비율% 이상의 할인이 있는 이모티콘을 모두 구매한다
        - 1 ≤ 비율 ≤ 40
    - 가격이상의 돈을 이모티콘 구매에 사용한다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입한다는 의미
        - 100 ≤ 가격 ≤ 1,000,000
        - 가격은 100의 배수
- 1 ≤ emoticons의 길이 = m ≤ 7
    - emoticons[i]는 i+1번 이모티콘의 정가를 의미
    - 100 ≤ emoticons의 원소 ≤ 1,000,000
    - emoticons의 원소는 100의 배수

<풀이 시간>
1시간

<풀이>
1. 할인율 조합 생성
2. 할인율 조합별 매출 및 구독자수 계산
3. 최대의 이익(구독자수, 매출) 업데이트

<시간 복잡도>
1. 중복순열(product)의 시간 복잡도: O(4 ** 이모티콘 개수)
2. calculate_profit 시간 복잡도: O(n)
-> 전체 시간 복잡도: O(4**이모티콘 개수) * O(n)
"""
from itertools import product


def calculate_profit(sales: tuple, users: list, emoticons: list):
    """
    :param sales: 각 이모티콘에 대한 할인율
    :param users: 각 사용자의 [비율, 가격]
    :param emoticons: 이모티콘 배열
    :return: sales(이모티콘에 대한 할인율)을 적용했을 때 얻는 구독자 수, 판매액
    """
    subscribers = 0 # 구독자수
    profits = 0 # 판매액
    for min_rate, limit_price in users:
        buy_amount = 0  # 사용자로부터 얻은 판매액
        for idx, sale in enumerate(sales):
            if sale >= min_rate:  # 할인율이 사용자가 원하는 할인비율 이상일 경우, 해당 이모티콘 구매
                buy_amount += (100 - sale) * emoticons[idx] / 100
            else: # 여기서 continue 해줘야 좀 더 빠름
                continue
        if buy_amount >= limit_price: # 사용자의 최대 구매액 이상이면 구독
            subscribers += 1  # 이모티콘 플러스 서비스 가입
        else:
            profits += buy_amount
    return subscribers, profits


def solution(users: list, emoticons: list) -> list:
    """
    :param users: 사용자 n명의 구매 기준을 담은 2차원 정수 배열
    :param emoticons: 이모티콘 m개의 정가를 담은 1차원 정수 배열
    :return: 행사 목적을 최대한으로 달성했을 때의 이모티콘 플러스 서비스 가입 수와 이모티콘 매출액
    """
    # 할인율
    discount_rate = [10, 20, 30, 40]
    emoticon_cnt = len(emoticons)
    max_subscriber = 0 # 최대 구독자 수
    max_profit = 0 # 최대 매출액

    # 1. 각 이모티콘의 할인율 경우의 수
    for sales in product(discount_rate, repeat=emoticon_cnt):  # O(4 ** 이모티콘의 개수) = 최대 O(4**7) = 16,384
        # 2. 할인율을 적용했을 때 모든 사람의 구매액 확인
        subscribers, profits = calculate_profit(sales, users, emoticons)
        # 3. 서비스 가입자가 더 많을 때 > 판매액이 최대일 때 업데이트
        if (subscribers > max_subscriber) or (subscribers == max_subscriber and profits > max_profit):
            max_subscriber = subscribers
            max_profit = profits

    return [max_subscriber, max_profit] # [이모티콘 플러스 서비스 가입 수, 이모티콘 매출액]
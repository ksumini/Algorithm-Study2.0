"""
<문제>
정수 배열 prices
prices[i]는 i번째 날의 주식 가격
각 날마다, 주식을 살지 팔지 결정해야 한다.
최대 한 주만 보유할 수 있고, 같은 날에 주식을 사서 바로 팔 수 있다.
이 때, 최대 이익을 구하라

<제한 사항>
1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104

<풀이 시간>
10분

<풀이>
매번 저점에서 매수 후 고점으로 바뀔때 매도

<시간복잡도>
O(n)
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
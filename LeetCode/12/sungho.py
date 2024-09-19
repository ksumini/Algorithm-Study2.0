class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0

        now_price = prices[0]

        for i in range(1, len(prices)):
            if now_price >= prices[i]:
                now_price = prices[i]
            else: # 현재 저장된 가격보다 prices[i] 가 높으면 차액 = 이익
                profit += prices[i] - now_price
                now_price = prices[i]

        return profit
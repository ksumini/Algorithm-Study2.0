class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_price = prices[0]
        profit = 0

        for price in prices[1:]:
            if price > cur_price:
                profit += price - cur_price
            cur_price = price
        
        return profit

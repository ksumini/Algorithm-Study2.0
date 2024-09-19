class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = prices[0]
        answer = 0
        for price in prices[1:]:
            if current < price:
                answer += price - current
        return answer



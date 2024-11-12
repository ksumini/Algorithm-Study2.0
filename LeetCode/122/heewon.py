class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        
        for i in range(len(prices)-1):
            total_profit += max(0, prices[i+1] - prices[i])
            
        return total_profit
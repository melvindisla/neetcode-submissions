class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = prices[0]
        profit = 0
        for price in range(1, len(prices)):

            if buy_day > prices[price]:
                buy_day = prices[price]
                
            elif prices[price] - buy_day > profit:
                profit = prices[price] - buy_day
        
        return profit
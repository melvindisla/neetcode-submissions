class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for price in prices[1:]:
            min_price = min(min_price, price)
            profit = max(price - min_price, profit)
        return profit
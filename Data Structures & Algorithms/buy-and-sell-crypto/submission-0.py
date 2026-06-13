class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = prices[0]
        max_profit = 0

        for r in range(len(prices)):
            current_profit = prices[r] - min_prices
            
            if prices[r] < min_prices:
                min_prices = prices[r]

            max_profit = max(current_profit, max_profit)
        return max_profit

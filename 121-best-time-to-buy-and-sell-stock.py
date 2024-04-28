class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]
        highest_price = 0
        for index, val in enumerate(prices):
            if val < lowest_price:
                lowest_price = val
                highest_price = 0
            if index + 1 < len(prices) and prices[index + 1] > highest_price:
                highest_price = prices[index + 1]
            if highest_price - lowest_price > max_profit:
                max_profit = highest_price - lowest_price
        return max_profit

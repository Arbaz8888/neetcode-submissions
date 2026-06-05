class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        max_profit = 0

        for i in range(len(prices)):

            if prices[i] < buy:
                buy = prices[i]
            else:
                curr_profit = prices[i] - buy
                max_profit = max(max_profit, curr_profit)
        
        return max_profit

        
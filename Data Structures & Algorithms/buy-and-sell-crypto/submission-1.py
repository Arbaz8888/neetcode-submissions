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

# 1) assign first element as buy
# 2) check second element, is it smaller than first, if yes then assign that as buy, if not check profit (second - first) and assign that max profit
# 3) third element, is it smaller than first, if yes then assign that as buy, if not check profit (second - first) and assign that max profit
"""
Say you have an array for which the i^th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

#method_1     双指针（88ms）
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        min_price = 2e29
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i] - min_price)
            if prices[i] < prices[i-1]:
                max_profit += profit
                min_price = prices[i]
                profit = 0
        max_profit += profit
        return max_profit

#method_2     该题仅要求最大利润，特殊方法（80ms）
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):  # 当天卖了还可以买，只需要判断后一天大于前一天
            max_profit += prices[i] - prices[i-1] if prices[i] > prices[i-1] else 0
        return max_profit


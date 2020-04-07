# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        holding_stock_price = float('inf')
        for price in prices:
            # Only sell if you can make a profit.
            if price > holding_stock_price:
                max_profit += price - holding_stock_price
            
            holding_stock_price = price
        return max_profit

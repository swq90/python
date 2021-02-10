class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        profit, min_price = 0, prices[0]
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                profit += price - min_price
                min_price = price
        return profit



    def maxProfit3(self, prices):
        if len(prices) < 2:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit






#允许多次交易
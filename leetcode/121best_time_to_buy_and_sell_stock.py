class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        profit, left, right = 0, 0, 1
        while right < len(prices):
            t = prices[right]-prices[left]
            if t > 0:
                profit = max(profit, t)
            elif t < 0:
                left = right
            right += 1
        return profit



    def maxProfit2(self, prices):
        if len(prices) < 2:
            return 0
        profit, min_price = 0, prices[0]
        for price in prices[1:]:
            min_price = min(min_price, price)
            profit = max(profit,price - min_price)
        return profit

# 第一个想到就是两个指针
    def maxProfit(self, prices):
        profit=0
        for buy in range(len(prices)-1):
            profit=max(profit,max(prices[buy+1:]))

        return profit

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if len(prices)<2:
            return 0

        dp=[]
        for i in range(len(prices)):
            for j in range(2):
                pass

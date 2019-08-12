class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sum + m * (n - 1) = x * n
        #x = min+m
        #因为无论如何进行add运算，最小值都必须参与其中
        #公式代入移项
        return sum(nums)-len(nums)*min(nums)
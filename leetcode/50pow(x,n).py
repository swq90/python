class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0.0:
            return 0
        if x == 1.0 or n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        return x**n
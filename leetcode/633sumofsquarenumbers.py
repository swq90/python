import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        return any(((c-a**2)**0.5)%1 == 0 for a in range(int(c**0.5)+1))
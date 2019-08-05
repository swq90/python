class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n:
            a,b = divmod(n,3)
            if not a and b==1:
                return True
            elif a and not b:
                n = a
            else:
                return False
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n:
            a, b = divmod(n,2)
            if a and b:
                return False
            if a == 0 and b ==1:
                return True
            if a:
                n = a

        return False


    def isPowerOfTwo2(self, n):
        return (n > 0) and (n & (n - 1)) == 0
    #二进制，&位运算
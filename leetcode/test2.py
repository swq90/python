class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b,c = 9,10,0
        t1 = 9*pow(10,c)(c+1)
        t2 = 0
        while n > t1:
            c += 1
            n -= t1
            t2 =0
        i,j =divmod(n,c+1)
        n = 9*pow(10,c)
# o = Solution()
# t = o.trailingZeroes(10000)#2499
print (ord('9'))
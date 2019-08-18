class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 0
        r = 0
        l=[]
        for i in range(2,n):
            j = 2
            while j<i/2:
                if i%j == 0:
                    break
                j += 1
            if j == i:
                r += 1
                l.append(i)
        print(l)
        return r

o = Solution()
print(o.countPrimes(10))
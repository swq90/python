class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # i,j = 5,2
        # r = 0
        # while i <= n:
        #     a = i
        #     while a:
        #         a,b = divmod(a,5)
        #         if b == 0:
        #             r += 1
        #         else:
        #             break
        #     i += 5
        # return r
        #要求时间复杂度，第一个方法太笨，找到规律就好了
        r = 0
        while n >= 5:
            n = n/5
            r += n
        return r
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = ""
        while n:
            r = chr(n%26+64) +r
            n //= 26
        return r


o =Solution()
print(o.convertToTitle(28))
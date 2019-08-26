class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = ""
        while n:
            n, m = divmod(n,26)
            m = max(m,1)
            r = chr(64+m)+r
        return r



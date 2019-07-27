class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = len(s) - 1
        r = 0
        for i in s:
            r += (ord(i) - 64) * pow(26, l)
            l -= 1

        return r

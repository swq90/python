class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        s = 1

        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                s = s+i+num//i
        return True if num == s else False


# 平方根


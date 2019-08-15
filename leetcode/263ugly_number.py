class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = [2, 3, 5]
        for i in l:
            while num % i == 0 and num > 1:
                num /= i

        return num == 1

# 不要忽略num为0的情况
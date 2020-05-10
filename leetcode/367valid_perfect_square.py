class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (int(num ** 0.5)) ** 2 == num

    def isPerfectSquare2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num
        while l <= r:
            m = (l + r) // 2
            if m * m == num:
                return True
            elif m * m < num:
                l = m + 1
            else:
                r = m - 1

        return False


o = Solution().isPerfectSquare2(9)
print(o)

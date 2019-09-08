# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 1
        while m < n :
            if isBadVersion((m+n)//2):
                n = (m+n)//2
            else:
                m =(m+n)//2 +1
        return n

# 二分法

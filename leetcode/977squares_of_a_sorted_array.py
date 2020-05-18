class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        z=[x * x for x in A]
        # z.
        return z.sort()
o=Solution().sortedSquares([-4,-1,0,3,10])
print(o)
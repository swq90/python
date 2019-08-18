class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        b = []
        for i in A:
            if i < 0:
                b.append(i)
            else:break

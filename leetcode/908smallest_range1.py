class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        x = max(A)
        y = min(A)
        if abs(x-y) <= 2*K:
            return 0
        return x-y-2*K
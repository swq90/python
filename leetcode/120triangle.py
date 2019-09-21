class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return ""
        total = 0
        for i in triangle:
            total += self.minimumTotal(triangle)
        return total
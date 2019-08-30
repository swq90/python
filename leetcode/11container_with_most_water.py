class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_c = 0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                max_c = max(max_c, min(height(i), height(j))*(j-i))
        return max_c

    def maxArea2(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res
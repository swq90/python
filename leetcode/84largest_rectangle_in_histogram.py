class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        area, l, r = 0, 0, len(heights)
        while l<r:
            area = max(min(heights[l:r])*(r-l), area)
            if heights[l]<=heights[r-1]:
                l += 1
            else:
                r -= 1
        return  area

o= Solution()
t = o.largestRectangleArea([5,5,1,7,1,1,5,2,7,6])
print(t)
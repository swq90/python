class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []

        for i in intervals[1:]:
            if not i:
                break
            if i[0] < res[-1][0]:
                res[-1][0] = i[0]
            elif i[0] <= res[-1][-1] and i[1]> res:
                res[-1][-1] = i[1]

            else:
                res.append(i)

        return res

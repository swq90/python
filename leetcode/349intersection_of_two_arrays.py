class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res =[]
        for i in set(nums1):
            t = min(nums1.count(i), nums2.count(i))
            res.extend([i]*t)
        return res


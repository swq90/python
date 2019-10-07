class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1),len(nums2)



o = Solution()
t = o.findMedianSortedArrays([0,1,2,3,4,5,6,10],[0,1,4,6,7])
print(t)
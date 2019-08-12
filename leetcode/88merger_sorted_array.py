class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0,0
        while i < m or j < n:
            if nums1[i] <= nums2[j]:
               i += 1
            else:
                nums1.insert(nums2[2],i)
                j += 1
        if j < n:
            nums1.extend(nums2[j:])
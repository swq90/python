class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1),len(nums2)
        i,j=0,n-1
        while i<m or j>=0:
            if nums1[i]<nums2[j]:
                if i+2<m & nums1[i+2]<nums2[j]:
                    i +=2
                elif i+2<m & nums1[i+1]<nums2[j]:
                    i+=1
                    j-=1
                else:




o = Solution()
t = o.findMedianSortedArrays([0,1,2,3,4,5,6,10],[0,1,4,6,7])
print(t)
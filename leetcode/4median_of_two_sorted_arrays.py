class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # m, n= len(nums1), len(nums2)
        # i,j,count = 0,0,0
        # median = (m+n)/2
        # while count<median-1:
        #     if nums1[i]<= nums2[j]:
        #         i += 1
        #     else:
        #         j += 1
        #     count += 1
        # print(i,j,nums1[i],nums2[j],count)
        # if median - count:
        #     return min(nums1[i],nums2[j])
        # return
        d = sorted(nums1+nums2)
        if len(d)/2:
            return d[len(d)//2]
        return (d[len(d)//2]+d[len(d)//2-1])/2


o = Solution()
t = o.findMedianSortedArrays([0,1,2,3,4,5,6,10],[0,1,4,6,7])
print(t)
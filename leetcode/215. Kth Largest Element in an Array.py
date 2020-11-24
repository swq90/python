class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return nums.sort()[-k]
d=[3,2,1,5,6,4]
k=2

print(d.sort())
# print(Solution().findKthLargest([3,2,1,5,6,4],2))
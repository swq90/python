class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not k:
            return []
        if not len(nums):
            return []
        if len(nums) < k:
            return [max(nums)]
        rt = []
        for i in range(len(nums) - k + 1):
            x = max(nums[i:i + k])
            rt.append(x)
        return rt

o = Solution()
t = o.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
print(t)
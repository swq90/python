class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = max(nums)
        for i in range(len(nums)-1):
            if not nums[i]:
                continue
            temp = nums[i]
            for j in range(i+1,len(nums)):
                if not nums[j]:
                    break
                temp *= nums[j]
                p = max(p,temp)
        return p


o = Solution()
t = o.maxProduct([-2,0,-1])
print(t)
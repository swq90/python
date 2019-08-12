class Solution:
    def missingNumber(self, nums) -> int:
        res =len(nums)*(len(nums)+1)/2-sum(nums)
        return int(res)
class Solution:
    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0
        res = [0, nums[0]]
        for i in range(1, len(nums)):
            res.append(max(res[i], res[i - 1] + nums[i]))
        return res[-1]

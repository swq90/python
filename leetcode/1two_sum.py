#twoSum 哈希，快90%


class Solution:
    def twoSum(self,nums, target):

        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)-1):
            need = target-nums[i]
            if (need in d) and (d[need] > i):
                return [i, d[need]]


    def twoSum2(self,nums, target):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]],i]
            else:
                d[target-nums[i]] = i

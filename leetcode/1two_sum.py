#twoSum 哈希，快90%


class Solution:
    def twoSum( nums, target):
        # l = []
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)-1):
            need = target-nums[i]
            if (need in d) and (d[need]>i):
                return [i,d[need]]



#
from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        res = [k for k, v in c.items() if v == 1]
        return res[0]



    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]

        nums.sort()
        # logging.debug(f"nums: {nums}")

        for i in range(0, len(nums) - 1, 2):
            if nums[i] == nums[i + 1]:
                # logging.debug(f"i: {nums[i]}")
                continue
            else:
                return nums[i]
        return nums[-1]

#异或运算

    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res = res ^ i
        return res

#set()对列表去重!
class Solution4(object):
    def singleNumber(self, nums):
        return sum(list(set(nums)))*2 - sum(nums)

class Solution(object):
    def removeElement(nums, val):
        if not nums:
            return 0
        elif val not in nums:
            return len(nums)
        else:
            nums[:] = [num for num in nums if num != val]
            return len(nums)


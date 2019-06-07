class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count, i = 0, 0
        d = nums[0]
        while i < len(nums):
            if nums[i] == d:
                if count < 2:
                    count += 1
                else:
                    nums.pop(i)
            else:
                d = nums[i]
                count = 1
        return len(nums)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        for i in range(len(nums)):
            if not nums[i]:

                if j == 0:
                    j = i + 1
                while j < len(nums) and (not nums[j]):
                    j += 1
                if j == len(nums):
                    return
                else:
                    nums[i], nums[j] = nums[j], nums[i]

#         j = 0
#         for i in range(len(nums)):
#             if nums[i]:
#                 if i != j:
#                     nums[i], nums[j] = nums[j], nums[i]
#                 j += 1


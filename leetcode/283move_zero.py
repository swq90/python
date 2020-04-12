class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,0

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

    def moveZeroes2(self, nums) -> None:
        d=nums.count(0)
        while d:
            nums.remove(0)
            nums.append(0)
            d-=1
nums=[0,1,0,3,12]
o=Solution().moveZeroes(nums)
print(o)
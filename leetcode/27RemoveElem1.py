class Solution:
    def removeElement1(self, nums: List[int], val: int) -> int:
        i = len(nums)-1
        while i >= 0:
            if nums[i] == val:
                nums.pop(i)
            i=i-1
        return len(nums)

    def removeElement2(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        elif val not in nums:
            return len(nums)
        else:
            nums[:] = [num for num in nums if num != val]
            return len(nums)


class Solution:
    def removeDuplicates(self, nums) -> int:
        count = 0
        if not nums:
            return count
        current_num = None
        current_idx = -1
        for x in nums:
            if x != current_num:
                new_idx = current_idx + 1
                nums[new_idx] = x
                current_num = x
                current_idx = new_idx
                count += 1
        nums = nums[0:count]
        return count


    def removeDuplicates1(self, nums: List[int]) -> int:
        count = 0
        if not nums:
            return count
        current_num = None
        current_idx = -1
        for x in nums:
            if x != current_num:
                new_idx = current_idx + 1
                nums[new_idx] = x
                current_num = x
                current_idx = new_idx
                count += 1
        nums = nums[0:count]
        return count

    def removeDuplicates3(self, nums: List[int]) -> int:
        t = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[t]:
                nums[i] = 'x'
            else:
                t = i
        nums[:] = [x for x in nums if x != 'x']
        return len(nums)

    def removeDuplicates4(self, nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)

o=Solution()
o.removeDuplicates([-1,0,0,0,0,3,3])

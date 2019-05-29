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


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        cur_length = 0
        for num in nums:
            if num:
                cur_length += 1
            else:
                max_length = max(max_length, cur_length)
                cur_length = 0
        return max(max_length, cur_length)

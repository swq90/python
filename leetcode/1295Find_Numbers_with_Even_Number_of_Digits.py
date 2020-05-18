class Solution:
    def findNumbers(self, nums) -> int:
        return len([x for x in nums if len(str(x))%2==0])





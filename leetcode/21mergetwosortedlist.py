# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if l1.val =
        l=None
        # l1.next,l2.next =0,0
        # while l1.next+l2.next !=len(l1.val)+(l2.val):
        #     if l1.v

        pass


    def maxSubArray(self, nums):
        if not nums:
            return None
        dp = [0] * len(nums)
        res = dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res


    # DP, constant space
    def maxSubArray2(self, nums):
        if not nums:
            return None
        loc = glo = nums[0]
        for i in range(1, len(nums)):
            loc = max(loc + nums[i], nums[i])
            glo = max(loc, glo)
        return glo
a = ListNode([1,2,4])
b = ListNode([0,3,4])

nums=[1,2,3,-1,7,-2,-3,2,4]
dp=[0]*len(nums)
print (dp)
print(a.val+b.val,a.next)
print(len(a.val))
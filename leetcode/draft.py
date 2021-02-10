# class Solution:
#     def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
#         def help(arr,target,res,ans):
#             print(arr,target,res,ans)
#             if target==0:
#                 ans.append(res)
#                 return
#             for i in range(len(arr)-1):
#                 if arr[i]>target:continue
#                 help(arr[i+1:],target-arr[i],res+[arr[i]],ans)
#         ans=[]
#         help(sorted(candidates),target,[],ans)
#         return ans

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 234. Palindrome Linked List
    def isPalindrome(self, head: ListNode) -> bool:
        pass

    # 4. Median of Two Sorted Arrays
    def findMedianSortedArrays(self, nums1: [int], nums2:[int]) -> float:
        # m,n=len(nums1),len(nums2)
        # p1,p2=m//2,n//2
        # l,r=p1+p2,m+n-p1-p2-2




print(Solution().sortArrayByParityII([4, 2, 5, 7]))

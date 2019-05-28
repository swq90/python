class Solution:
    def searchInsert1(self, nums: List[int], target: int) -> int:
        list.append(target)
        list.sort()
        n = list.index(target)
        return n


    def searchInsert2(self, nums: List[int], target: int) -> int:
        l,r =0,len(nums)-1
        while l <= r:
            n = (l+r)//2
            if nums[n] == target:
                return n
            elif nums[n] > target:
                r = n - 1
            else:
                l = n+1
        return l    #target not in nums
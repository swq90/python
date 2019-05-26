#twoSum 哈希，快90%

# def twoSum1(nums):
#     l = []
#     d = {}
#     for i in range(len(nums)):
#         d[nums[i]] = i
#         # d1 = d.copy()
#         # l.append(d1)
#     print(d)
# nums = [3,2,4]
# print(twoSum1(nums))
class Solution:
    def twoSum( nums, target) :
        # l = []
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        # l1 = sorted(l, key=lambda e: e['key'])
        # for i in range(len(l1)-1):
        # nums.sort()
        # print(nums)
        for i in range(len(nums)-1):
            need = target-nums[i]
            if  (need in d) and (d[need]>i):
                return [i,d[need]]


nums = [1,7,6,3,22,11,2]
target = 3
print(Solution.twoSum(nums,target))
class Solution:
    def fourSum(self, nums, target: int):
        n = sorted(set(nums))
        pre = []
        for i in range(len(nums)):

            pre =[x+y for x in pre for y in n[i:]]
        return
nums = [1,0,-1,0,-2,2]
target = 0
n = set(nums)
print (n)
pre = []
for i in range(len(nums)):
    pre = [x + y for x in pre for y in n[i:]]

print (pre)

from functools import reduce


def productExceptSelf( nums):
    if nums.count(0)>1:
        return [0]*len(nums)
    if nums.count(0)==1:

        n=nums.index(0)
        nums.pop(nums.index(0))
        z=reduce(lambda x,y:x*y,nums)

        return ([0]*(len(nums)-1)).insert(nums.index(0),reduce).res.insert(n,z)
#     #
#     # product=reduce(lambda x,y:x*y,nums)
#     # return [int(product/x) for x in nums]

    for i in range(len(nums)):
        return


d=[1,2,3,0,4,3]
print((d.pop(2)))
print([0]*2)
print(productExceptSelf(d))
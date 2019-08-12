class Solution:
    def threeSum( nums) :
        res = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    s =[nums[i],nums[j],nums[k]]
                    if (sum(s) == 0) & (s.sort() not in res):

                        print(s)

                        res += [s]
        return res

print(Solution.threeSum([-1,0,1,2,-1,-4]))
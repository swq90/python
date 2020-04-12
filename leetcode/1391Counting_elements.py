class Solution:
    def countElements(self, arr) :
        nums=[x+1 for x in arr]
        count=0
        for x in nums :
            if x in arr:
                count+=1
        return count

o=Solution()
x=[1,1,3,3,5,5,7,7]
print(o.countElements(x))
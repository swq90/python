class Solution:
    def combinationSum(self, candidates, target: int) :
        def helper(arr,target,res,ans):
            print(arr,target,res,ans)
            if target==0:
                ans.append(res)
            for i in range(len(arr)):
                if arr[i]>target:continue
                helper(arr[i:],target-arr[i],res+[arr[i]],ans)
        ans=[]
        helper(candidates,target,[],ans)
        return ans


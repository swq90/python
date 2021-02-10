class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        def help(arr,target,res,ans):
            print(arr,target,res,ans)
            if target==0:
                ans.append(res)
                return
            for i in range(len(arr)-1):
                if arr[i]>target:continue
                help(arr[i+1:],target-arr[i],res+[arr[i]],ans)
        ans=[]
        help(sorted(candidates),target,[],ans)
        return ans
# 怎么处理重复的组合
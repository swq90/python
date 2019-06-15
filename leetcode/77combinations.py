class Solution:
    def combine( n: int, k: int) :
        res = [[]]
        for i in range(k):
            res = [t+[c] for t in res for c in range(1,t[0] if t else n+1) ]


        return res

print(Solution.combine(4,2))
# d = [[], [], 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
# for i in digits:
#     r = [pre + cur for pre in r for cur in d[int(i)] ]
class Solution:
    def findJudge(self, N: int, trust) -> int:
        citizens=set([trust[x][0] for x in range(len(trust))])
        print(citizens)

        if len(citizens)==N or len(citizens)<N-1:

            return -1

        judge={}
        print(sorted(trust))
        for r in trust:
            if r[1] not in citizens:
                judge[r[1]].append(r[0])
        for k,v in judge.values():
            if len(set(v))==N-1:
                return k
        return -1



o=Solution().findJudge(4,[[1,3],[1,4],[2,3]])
print(o)
# graph
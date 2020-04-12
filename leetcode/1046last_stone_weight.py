from collections import Counter
class Solution:
    def lastStoneWeight(self, stones) :

        while len(stones)>1:
            stones.sort()
            if stones[-2]==stones[-1]:
                stones.pop()
                stones.pop()
            else:
                stones[-1]=stones[-1]-stones[-2]
                stones.pop(-2)
        return stones[0] if stones else 0

    def lastStoneWeight1(self, stones) :

        d=Counter(stones)



o=[1,2,2,1,4,3,6,6,2,2,3]
print(o.count())
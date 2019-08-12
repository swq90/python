class Solution:

    def letterCombinations(self, digits: str) :
        if len(digits) == 0:
            return []
        r =[]
        d = [[],[],'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        for i in digits:
            r = [pre + cur for pre in r for cur in d[int(i)]]
        return  r


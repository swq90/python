class Solution:
    def generate(self, numRows: int) :
        t=[[1]*i for i in range(1,numRows+1)]
        if numRows<3:
            return t
        i = 2
        while i <numRows:
            j = 1
            while j<i:
                t[i][j] =t[i-1][j-1]+t[i-1][j]
                j +=1
            i += 1
        return t

    def generate2(numRows):
        pascal = [[1] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal   
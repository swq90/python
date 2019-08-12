class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        x = 1
        res =[]
        for i in range (numRows):
           res.append('')
        r = ''
        j = 0
        for i in s:
            res[j] += i
            if j == numRows - 1:
                x = -1
            elif j == 0:
                x = 1
            j += x
        for i in res:
            r += i
        return r


    def convert2(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        x, j = 1, 0
        res =['']*numRows
        r = ''
        j = 0
        for i in s:
            res[j] += i
            if j == numRows - 1:
                x = -1
            elif j == 0:
                x = 1
            j += x

        return ''.join(res)

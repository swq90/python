class Solution:
    def getRow(self, rowIndex):
        t = [[1] * (i + 1) for i in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            for j in range(1, i):
                t[i][j] = t[i - 1][j - 1] + t[i - 1][j]

        return t[rowIndex]
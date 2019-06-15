class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        for i in range(len(matrix)-1):
            for j  in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True

    def isToeplitzMatrix2(self, matrix) -> bool:
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:#
                return False
        return True

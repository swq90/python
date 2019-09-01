class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


    #  + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。 重复列表
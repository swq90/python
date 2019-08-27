class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        d = {'U': 1, 'D': -1, 'L': 2, 'R': -2}
        s = 0
        for i in moves:
            s += d[i]
        if not s:
            return True
        return False





    # return (moves.count('D') == moves.count('U') and moves.count('L') == moves.count('R'))
    #discuss方法……
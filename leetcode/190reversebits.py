class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = int(n,2)
        s = ''
        while n:
            n,a = divmod(n,2)
            s += str(a)
        s = bin(s)
        return s


o =Solution()
o.reverseBits(00000010100101000001111010011100)
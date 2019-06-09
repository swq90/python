class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        while x or y:
            t = (x%2)^(y%2)
            distance += t
            x //=2
            y //=2
        return distance

    def hammingDistance2(self, x: int, y: int) -> int:
        distance = 0
        t = x ^ y
        while t:
            if t & 1:
                distance += 1
            t = t >> 1
        return distance




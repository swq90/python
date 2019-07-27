class Solution:
    def mySqrt(self, x: int) -> int:
        if x = 0
        t = x / 2
        while pow(t,2) > x:
            t /= 2

        while pow(t,2) <= x:
            if pow(t+1,2) >= x:
                return t
            t += 1

o=Solution()
o.mySqrt(1)

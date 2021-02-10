class Solution:
    def mySqrt(self, x: int) -> int:
        left,right=0,x
        while left<=right:
            mid=(left+right)//2
            if mid**2<=x <(mid+1)**2:
                return int(mid)
            elif mid**2>x:
                right=mid
            else:
                left=mid if left<mid else mid+1

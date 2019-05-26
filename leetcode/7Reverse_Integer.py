class Solution:
    def reverse( x: int) -> int:
        sign=1
        if x<0:
            sign=-1
        s=0
        x=abs(x)
        while x>0:
            s=s*10+x%10
            x=x//10
        result=s*sign
        if (result < -(2**31))or(result >= 2**31):
            return 0            
        else:
            return result

Solution.reverse(-321)
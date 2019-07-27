class Solution:
    def climbStairs(self, n: int) -> int:
        a,b,x,y,count = 1,2,0,0,0
        while n-b*x >= 0:
            y = n- b*x
            if y :
                count += (x+1)*y
            else:
                count += 1
            x += 1
        return count



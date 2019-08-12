class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        low,high = 0,n

        # t1 = int((low+1)*low/2)
        # t2 = int((high+1)*high/2)
        while low < high:
            mid = (low+high)//2
            t = (mid+1)*mid//2
            if n > t:
                low = mid+1
            elif n <t:
                high = mid-1
            else:
                return mid

        print(low,high,mid)
        return low-1
o= Solution()
print(o.arrangeCoins(5))
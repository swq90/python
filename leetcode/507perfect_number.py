class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        s = 1
        #l = [1,]#i not in l and
        for i in range(2,num//4+1):
            if (num//i)*i == num:
                # l.append(i)
                # l.append(num//i)
                s = s+i+num//i
                if s > num:
                    return False
        return True if num == s else False
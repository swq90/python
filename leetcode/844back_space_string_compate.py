class Solution(object):
    def dels(self,s):
        while i<len(s):
            if s[i] =="#" :
                s[i] ==''
                if i:
                    s[i-1] == ""
                    i -= 1
            else:
                i += 1
        return s
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S[:] = dels(S)
        T[:] = dels(T)
        if S == T:
            return True
        return False
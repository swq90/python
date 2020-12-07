class Solution(object):
    def isValid(self, s):
        if len(s) % 2:
            return False
        str_in = []
        d = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in d:
                str_in.append(i)
            else:
                if not str_in: return False
                if d[str_in[-1]] == i:
                    str_in.pop(-1)
                else:
                    return False
        if str_in: return False
        return True


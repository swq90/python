class Solution:
    def romanToInt(self, s):
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result=0
        while len(s):
            #s[1]可能出现下标越界的情况，字符串的操作
            if (len(s) != 1) and (d[s[0]] < d[s[1]]):
                result = result+ d[s[1]]-d[s[0]]
                s = s[2:]
            else:
                result = result + d[s[0]]
                s = s[1:]

        return result



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not len(s):
            return True
        if len(s)%2:
            return False
        stack = ""
        d = {'(':')','[':']','{':'}'}
        i = 0
        while i <len(s):
            if s[i] in d.keys():
                if d[s[i]] == s[i+1]:
                    i += 2
            if s[i]:
                pass
        # for i in s:
        #     if i in "([{":
        #         stack += i
        #     elif i == ")" and stack[-1]=="(":
        #         stack[:] = stack[:-1]
        #     elif i == "}" and stack[-1] == "{":
        #         stack[:] = stack[:-1]
        #     elif i == "]" and stack[-1] == "[":
        #         stack[:] = stack[:-1]
        #     else:
        #         return False

        return True

o=Solution()
print(o.isValid("()[]{}"))
class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l % 2:
            return False
        d = {'(': ')', '[': ']', '{': '}'}
        for i in range(0, l - 2, 2):
            if d[i] != s[i + 1]:
                return False

        return True

o=Solution()
print(o.isValid("()[]{}"))
class Solution:
    def firstUniqChar(self, s: str) -> int:
        t=''
        for i in range(len(s)):
            if (s[i] not in s[i+1:])&(s[i] not in t):
                return i
            t+=s[i]
        return -1

o=Solution()
print(o.firstUniqChar('ooaadc'))
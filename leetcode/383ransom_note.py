import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=collections.Counter(ransomNote)
        m=collections.Counter(magazine)
        for i in r.keys():
            if i in m.keys():
                if r[i]>m[i]:
                    return False
            else:return False

        return True

o=Solution()
print(o.canConstruct("aa",
"ab"))
class Solution:
    def strStr1(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        i = 0
        while (i+len(needle))< len(haystack):
            t = i
            j = 0
            while haystack[t] == needle[j]:
                t += 1
                j += 1
                if j == len(needle) :
                    return i
            i += 1
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        i = 0
        while (i + len(needle)) <= len(haystack):
            if haystack[i:i + len(needle)] == needle:
                return i
            i += 1
        return -1



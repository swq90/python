class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split(' ')
        d = dict(zip(strs, [None] * len(strs)))
        for i in range(len(pattern)):

            if d[pattern[i]]:
                if d[i] != strs[i]:
                    return False
            else:
                d[pattern[i]]=strs[i]

        return True


o = Solution()
t = o.wordPattern("abba","dog cat cat dog cat dog")
print(t)
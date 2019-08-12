class Solution:
    def countAndSay( n: int) -> str:
        if n == 1:
            return '1'
        s = '1'

        while n-1:
            s1 = ''
            t = ''
            count = 0
            for i in range(len(s)):
                if s[i] == t:
                    count += 1
                else:
                    if count:
                        s1 += str(count) + t

                    t = s[i]
                    count = 1
            s1 += str(count) + t
            s = s1
            n -= 1
        return s




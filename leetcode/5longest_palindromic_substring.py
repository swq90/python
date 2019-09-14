class Solution(object):
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        if len(s)==len(set(s)):
            return s[0]
        if set(s)==1:
            return s
        answer = ''
        for i in range(len(s)):

            for j in range(len(s)-1,i,-1):

                m,n = i,j
                while m < n:
                    if s[m] == s[n]:
                        m += 1
                        n -= 1
                    else:
                        break
                if m >= n:
                    temp=s[i:j+1]
                    if len(temp)>len(answer):
                        answer = temp
        if not answer:
            answer= s[0]
        return answer


    def longestPalindrome2(self, s):
        if len(s)<=1:
            return s
        if len(s)==len(set(s)):
            return s[0]
        if set(s)==1:
            return s
        answer= s[0]
        for length in range(len(s),1,-1):
            i = 0
            while i+length<=len(s):
                mid = length//2
                print(s[i:mid],s[i+length-1:i+mid-1:-1])
                if s[i:i+mid]==s[i+length-1:i+length-1-mid:-1]:
                    answer=s[i:i+length]
                    return answer
                i += 1
        return answer




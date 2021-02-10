class Solution:
    def isPalindrome(self, s,l,r):
        while l<r and s[l]==s[r]:
            l+=1
            r-=1
        if l<r:return False
        return True


    def longestPalindrome(self, s: str) -> str:
        for l in range(len(s)-1, 0, -1):
            for i in range(len(s) - l ):
                if self.isPalindrome(s,i,i+l):
                    return s[i:i+l+1]

        return s[0]
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t = s.split()
        if len(t):
            return len(t[-1])
        else:
            return  0
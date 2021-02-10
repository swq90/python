class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a,b=0,0
        for i in guess:
            if i in secret:b+=1

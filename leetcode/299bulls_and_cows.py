class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a,b = 0,0
        for m in range(len(guess)):
            if guess[m] == secret[m]:
                a += 1
            elif guess[m] in secret:
                b += 1
        return 
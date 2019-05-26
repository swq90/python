class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        s = 0
        y = x
        while x != 0:
            s = x % 10 + s * 10
            x = x // 10
        if s == y:
            return True
        else:
            return False

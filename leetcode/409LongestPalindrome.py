class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = [s.count(i) for i in set(s)]
        res = list(map(lambda x: x - 1 if x % 2 else x, res))
        print(res)
        if sum(res) < len(s):
            return sum(res) + 1
        return len(s)

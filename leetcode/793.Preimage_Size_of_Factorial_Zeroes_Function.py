class Solution:

    def preimageSizeFZF(self, K: int) -> int:
        def trailingZeroes(n):
            """
            :type n: int
            :rtype: int
            """
            r = 0
            while n >= 5:
                n = n // 5
                r += n
            return r

        l, r = 0, 5 + 5 * K
        while l < r:
            mid = (l + r) // 2
            t = trailingZeroes(mid)
            if t == K:
                return 5
            elif t < K:
                l = mid + 1
            else:
                r = mid
        return 0

# 数学题，第一反应答案只有0or5，可利用172题+二分
# 右边界没有直接用无穷，5*K足够了，忘记了K=0

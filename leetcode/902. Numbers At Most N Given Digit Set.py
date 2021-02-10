class Solution:
    def atMostNGivenDigitSet(self, digits: [str], n: int) -> int:
    #     res = []
    #     len_digits=len(digits)
    #     len_n=len(str(n))
    #     for _ in range(len_n-1):
    #         res.append(len_digits) if not res else res.append(len_digits*res[-1])
    #     # if n==10**(len_n-1):return sum(res)
    #     res.append(len([x for x in digits if x<str(n)[0]])*res[-1])
    #     if str(n)[0]  in digits:
    #         x=[str(n)[0]]*len_digits
    #         for _ in range(len_n-1):
    #             x=[j+i for j in x for i in digits ]
    #         res.append(len([i for i in x if i<=str(n) ]))
    #     return sum(res)
    # # 时间
        up, ans, T, str_n = [0] * 10, 0, len(digits), str(n)
        for i in range(10):
            for dig in digits:
                up[i] += (dig < str(i))

        k, d_set = len(str_n), set(digits)
        for i in range(k):
            if i > 0 and str_n[i - 1] not in d_set: break
            ans += up[int(str_n[i])] * T ** (k - i - 1)

        addon = (T ** k - 1) // (T - 1) - 1 if T != 1 else k - 1
        return ans + addon + (not set(str_n) - set(digits))





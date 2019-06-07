class Solution:
    def addToArrayForm1( A, K) -> [int]:#180ms
        k = []
        s = 0
        while K:
            t = K % 10
            k.insert(0, t)
            K //= 10
        for i in range(1, len(k) + 1):
            if len(A) < len(k):
                A.insert(0, 0)
            A[-i] = A[-i] + k[-i]
        for i in range(1, len(A) + 1):
            if A[-i] + s > 9:
                if i == len(A):
                    A.insert(0, 1)
                A[-i] = (A[-i] + s) % 10
                s = 1
            else:
                A[-i] += s
                s = 0
        return A

#
# print(Solution.addToArrayForm([2,1,5],806))
#     def addToArrayForm2( A, K) -> [int]:
#         t= len(A)
#         while K:





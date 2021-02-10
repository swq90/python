def sortArrayByParityII(self, A: [int]) -> [int]:
    for k in range(0, len(A), 2):
        if A[k] % 2 != 0:
            for j in range(1, len(A), 2):
                if A[j] % 2 == 0:
                    t = A[k]
                    A[k] = A[j]
                    A[j] = t
                    break
    return A

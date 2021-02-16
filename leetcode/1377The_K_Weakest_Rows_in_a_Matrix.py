from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {i: sum(mat[i]) for i in range(len(mat))}
        res = sorted(d, key=d.get)
        return res[:k]


o = Solution()
print(o.kWeakestRows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], 3)
      )

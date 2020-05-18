class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i =0
        while i <(len(arr)):
            if arr[i]:
                i+=1
                continue
            arr.pop(            )
            arr.insert(i,0)
            i+=2
    def duplicateZeros2(self, arr) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0

o=Solution().duplicateZeros2([1,0,2,3,0,4,5,0])
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: 'I',5: 'V', 10: 'X', 50: 'L', 100:'C' , 500: 'D', 1000: 'M'}
        k=[1000, 500, 100, 50, 10, 5, 1]
        l =[]
        s=''
        m = 0
        for i in k:
            t=num//i
            l.append(t)
            num %=i
        while m < 7:

            if l[m] == 1:
                if l[m + 1] == 4:
                    s += d[k[m + 1]] + d[k[m - 1]]
                    m += 2
                    continue
                else :
                    s += d[k[m]]
            elif l[m] and m != 6:
                s += d[k[m + 1]] + d[k[m - 1]]

            else:
                while l[m]:
                    s += d[k[m]]
                    l[m] -= 1

            m += 1
        return s

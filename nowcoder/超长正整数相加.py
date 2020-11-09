a1, a2 = input(), input()
if len(a1) < len(a2):
    a1, a2 = a2, a1
a2 = '0' * (len(a1) - len(a2)) + a2
t, res = 0, ''
for i in range(len(a1) - 1, -1, -1):
    x = int(a1[i]) + int(a2[i]) + t
    t = x // 10
    res = str(x % 10) + res
if t:
    res = str(t) + res
print(res)
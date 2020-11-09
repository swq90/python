x, y = input(), input()
if len(x) < len(y):
    x, y = y, x
y = '0' * (len(x) - len(y)) + y
h = list(zip(x, y))
res = []
m = 0
for i in h[::-1]:
    s = int(i[0]) + int(i[1]) + m
    if s // 10:
        m = s // 10
        s = s % 10
    else:
        m = 0
    res.insert(0, s)
if  m:
    res.insert(0, m)
print(''.join(map(str, res)))
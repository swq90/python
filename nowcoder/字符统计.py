line = input()
d = {}
res = ''
for c in set(line):
    if line.count(c) not in d:
        d[line.count(c)] = ''
    d[line.count(c)] += c

dd = sorted(d, reverse=True)
for i in dd:
    res += ''.join(sorted(d[i], key=ord))
print(res)
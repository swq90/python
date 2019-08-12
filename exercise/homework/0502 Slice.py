L=[]
i=1
while i<=100:
    L.append(i)
    i=(i+1)**2
print(L)
def trim(s):
    if len(s)==0:
        return s
    while s[0]==" ":
        s=s[1:]
        if len(s)==0:
            return s
    while s[-1]==" ":
        s=s[:-1]
        if len(s)==0:
            return s
    print(s)
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

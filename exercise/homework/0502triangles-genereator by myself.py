L1=[1]
L2=[2]
L=[L1+L2]#得到的list含L1 L2组合的小list

print(L)
L.append(0)
print(L)
print(len(L))
for i in range(len(L)):
    print (i)

#杨辉三角
def triangles():
    l=[1]
    yield l

    while 1:
        l.append(0)#错误原因，此时临时t->l地址变为[1,0] ,执行到yield时重新赋予[1,1],但是再次循环依然面对这个问题
        l=[l[i-1]+l[i] for i in range(len(l))]#列表生成器，重新分配地址生成新list，所以解决末尾加“0”，要在列表生成器中或者之后实现杨辉三角的构造
        yield l

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
print(results)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')


def triangles2():

    l = [1]

    while 1:

        yield [x for x in l]
        l.append(0)
        l=[l[i-1]+l[i] for i in range(len(l))]

n = 0
results = []
for t in triangles2():
    print(t)
    results.append(t)
    print('cc',results)
    n = n + 1
    if n == 10:
        break
print(results)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
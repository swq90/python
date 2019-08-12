# 不必创建完整的list，从而节省大量的空间。这种一边循环一边计算的机制，称为生成器：generator。
#方法一：列表生成式的[]改成()，就创建了一个generator：
L=[x*x for x in range(10)]
G=(x*x for x in range(10))
print(L)
print(G)#
print(next(G))#每一个next 获得下一个G的返回值,太麻烦
print(next(G))
print(next(G))

G2=(x*x for x in range(10))
for n in G2:
    print(n)


#杨辉三角
def triangles():
    L = [1,1]
    loopn = 0;
    while 1:  # 1为真，进入持续循环
        yield 1  # 输出数组，跳出，跳回从下一步执行
        yield [1,1]
        yield list(L[loopn-3]+L[loopn-2])
        loopn = loopn +10   
        #L = [L[i - 1] + L[i] for i in range(len(L))]
        #print("gg",L)


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
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


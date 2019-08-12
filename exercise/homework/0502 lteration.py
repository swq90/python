#除了 list tuple str,可以用collections的Iterable判断是否可以迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d :
    print (value)
#默认迭代key，迭代value方法如下
for value in d.values():
    print (value)
# 同时迭代
for k,v in d.items():
    print (k,v)
print(d)
from collections.abc import Iterable
if isinstance("afljf",Iterable):
    print('yes')
    #  Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated
    # so,将collections加.abc
#实现类似java 的下标循环 enumerate
for x,y in enumerate(['a','c','e']):
    print(x,y)
#用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if len(L)==0:
        return(None,None)
    min=L[0]
    max=L[0]
    for x in L:#第一次错误，注意区分 for 和 while
        if x<min:
            min=x
    for y in L :
        if max< y:
            max=y
    return (min, max)


def abc(L):
    g=0
    while len(L) > g:
        print("abc",L[g])
        g=g+1

l=[1,2,3]
abc(l)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

def findMinAndMax(L):
    if len(L)!="":
        (min,max) =(L[0],L[0])
        for x in L:  # 第一次错误，注意区分 for 和 while
            if x < min:
                min = x
            if max < y:
                max = y
        return (min, max)
    else:
        return (None, None)



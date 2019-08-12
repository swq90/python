#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
sorted([36, 5, -12, 9, -21], key=abs)
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
#key函数仅帮助排序，只是排序依据

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()

L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return -t[-1]
L2 = sorted(L, key=by_score)
print(L2)
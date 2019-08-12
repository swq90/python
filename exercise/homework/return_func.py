def lazy_sum(*args):
    def sum():#内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
        # 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 4, 5, 7, 8, 9)

print('返回求和函数而不是结果',f)

print('调用时才计算结果输出',f())

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print('f1=',f1())
print('f2=',f2())
print(f1==f2)#调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数,f1()和f2()的调用结果互不影响
#因为存储位置不一样么?
print(f1)
print(f2)
print(f1()==f2())
# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
#函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
# 所以，闭包用起来简单，实现起来可不容易。
#另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print('count',list(count()))#为什么时位置？
print(f1())
print(f2())
print('f3',f3())
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

#如果一定要引用循环变量，方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
# fix:

def count():
    fs = []
    def f(n):
        def j():#新建函数，
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))

    return fs

f1, f2, f3 = count()

print(f1())

print(f2())

print(f3())
#一个函数可以返回一个计算结果，也可以返回一个函数。
#返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
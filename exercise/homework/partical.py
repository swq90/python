import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))#
int2('10010')
#把某个参数固定，相当于设置默认参数
#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入int2 = functools.partial(int, base=2)
#实际上固定了int()函数的关键字参数base，也就是：
int2('10010')
# 相当于：
# kw = { 'base': 2 }
# int('10010', **kw)
# 当传入：
# max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：
# max2(5, 6, 7)
# 相当于：
# args = (10, 5, 6, 7)
# max(*args)
# 结果为10。



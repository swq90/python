# 计算圆周率可以根据公式：
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：
import itertools
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natual=itertools.count(1,2)#count(start,step)有步长
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns=list(itertools.takewhile(lambda x: x<=2*N,natual))
    # l=itertools.takewhile(lambda x: x%2==1,ns)  #?????x%2==1有问题？
    # for i in l:
    #     print(i)
    sum=0
    for x in ns:
        if x%4==1:#奇数列
            sum=sum+4/x
        else:
            sum=sum-4/x
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: 求和:

    return sum

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

#
# def pi(n):
#     a = 1   # 这是为了后面符号做准备
#     s = 0   # 这是为了返回结果做准备
#     for i in itertools.count(1):    # 利用itertools.count生成无限序列，从1开始
#         if i > 2*n:     # 跳出循环
#             return s
#         if i % 2 == 1:  # 奇数
#             s += (4/i)*a     # 直接求和
#             a = -a

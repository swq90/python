#函数 f=x*x
def f(x):
    return x*x

r=map(f,[1,2,3,4])
print(list(r))

r=map(str,[1,2,3,4])
print(list(r))

#reduce()函数
#把一个函数作用于一个序列，这个函数必须接收两个参数
#reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)

from functools import reduce
def add(x,y):
    return x+y

print(reduce(add,[1,2,3,4]))


#把序列[1,2,3,4]变换为1234
def fn(x,y):
    return x*10+y

print(reduce(fn,[1,2,3,4]))


#利用map，规范用户名输入
def normalize(name):
    return name[0].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    return reduce(lambda x,y:x*y,L)#用lambda 即表达式
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':.}
    



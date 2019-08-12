#函数名是指向一个函数对象的引用，因此可以把函数名赋值给一个变量
a=abs
print(a(-11))
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
def nop():
    pass#定义空函数，什么也不做，pass做占位符
age=10
if age>18:
    pass#没有pass会报错

def myabs(x):
    if not isinstance(x,(int,float)):
       raise TypeError('bad operand type ')#添加参数检查
    if x>0:
        return x
    else:
        return -x
y=-1
# #y=input("input the num:")
#y='abc'
print(myabs(y))
import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny
x,y=move(0,0,10,math.pi/6)
print(x,y)
r=move(0,0,9,math.pi/6)
print(y)
print(r)#看结果可知返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，
# 按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
def quadratic(a, b, c):
    y=b**2-4*a*c
    if y<0:
        print('no answer')
    else:
        x1=(-b+math.sqrt(y))/(2*a)
        x2=(-b-math.sqrt(y))/(2*a)
        return x1,x2
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
def enroll(name,gender,age=6,city='nanjing'):
    print("name:",name)
    print("gender:",gender)
    print('age:',age)
    print('city:',city)
enroll("jane",'f')
enroll("bob",'m',8)
#enroll('bell','m',,"beijing")
enroll('amy','f',7,'tokoyo')
enroll('wendy','f',city='tianjin')#不按顺序时要把参数名写上

def addend(L=[]):
    L.append("end")
    return L
print(addend([1,2,3]))
print(addend())
print(addend())
print(addend())#默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容
# 则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了,解决办法如下None
def addend2(L=None):
    if L is None:
        L=[]
    L.append('end')
    return L
print(addend2([1,2,3]))
print(addend2())
print(addend2())
print(addend2())

def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
num=(1,2,3)
print(calc(num))
print(calc((1,2,3)))
print(calc([0]))
#print(calc((0)))tuple不能接受
t=(0,)#tuple不能用（？）
print(t)
print(calc(t))

def calc2(*numbers):#加*变可变参数，numbers 接收到是tuple
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print(calc2(1,2,3))#接收到是tuple，不用再重新组件list or tuple
print(calc2(num[0],num[1],num[2]))
print(calc2())#可以直接计算无参数
print(calc2(*num))#*num表示把num所有元素作为可变参数传进去
#关键字参数
def person(name,age,**kw):#kw为关键字参数
    print("name:",name,'age:',age,"other:",kw)#关键字参数允许你传入0个或任意个含参数名的参数，
    # 这些关键字参数在函数内部自动组装为一个dict。
person("jane",18)#可以只传入必选参数
person("vicky",18,city="bj",hobby="reading")#也可以传入任意个关键字参数
extra={'city':'beijing',"job":'engineer'}#关键字参数可以扩展函数功能，除了必填外其他是可以是选填
#与可变函数类似，可以先组装一个dict，然后转换为关键字参数传入
person("jason",28,city=extra['city'],job=extra["job"])#意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
person("jason",27,**extra)#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
#命名关键字参数
#举例，要检查person中是否有 city job 两个参数？
def person(name,age,**kw):
    if "city" in kw:
        pass
    if "job" in kw:
        pass
    print("name:", name, 'age:', age, "other:", kw)
person ("jack",22,address='chaoyang')
#要限制关键字参数，就用命名关键字参数，例如只接受 city job
def person(name,age,*,city,job):
    print(name,age,city,job)
person('jack',22,city='nanjing',job='sportman')
#person('jack',22,city='nanjing',adress='chaoyang')
def person(name, age, *args, city, job):#函数中已经有可变参数，后面的命名关键字参数不需要*
    print(name, age, args, city, job)
others=("chaoyang",'123456','133*****')
person("j",11,*others,city="nj",job="s")
#参数组合
#必选，默认，可变，关键字命名关键字，五类参数组合使用
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1,2)
f1(1,2,c="three")
l=[10,0,0]
f1(1,2,0,*l,name="jj")
f2(1,1,d="?",name="jj",address="chaoyang")
d={"who":"jj","when":"yesterday"}
#f2(1,1,1,*l,**d)#错误原因👇
f2(1,1,1,d=l,**d)#命名关键字要写参数名
#作业：允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积
def product(x, y):
    return x * y
print(product(11,2))
def product(*nums):
    p=1
    for n in nums:
        p=p*n
    return p

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
#小结
#Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#要注意定义可变参数和关键字参数的语法：
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。
#以及调用函数时如何传入可变参数和关键字参数的语法：
#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数
#递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
#防止栈溢出，尾递归优化
def fact(n):
    return factiter(n,1)
def factiter(num,product):
    if num==1:
        return product
    return factiter(num-1,num*product)
#返回时调用本身，且不含表达式
print(fact(5))




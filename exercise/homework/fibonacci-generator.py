def fib(max):
    n,a,b=0,0,1#三个变量赋值
    while n < max:
        yield (b) #打印的一个数
        a , b = b , a + b #小兔子=上月大兔子，大兔子=上月大+小兔子
        n=n+1
        return "done"


fib (6)
L1=[1]
L2=[2]
L=[L1+L2]
print(L)
L.append(0)
print(L)
print(len(L))
for i in range(len(L)):
    print (i)
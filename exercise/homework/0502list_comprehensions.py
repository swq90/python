
L=[x*x for x in range(1,11,1)if x%2==0]
print( L)
m=[m+n for m in "abc"  for n in "ABC" ]
print(m)
#
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[]
for i in L1:
    if isinstance(i,str):#方法一，常规，非列表生成式
        L2.append(i.lower())

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
L2=[i.lower() for i in L1 if isinstance(i,str)]#列表生成式
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
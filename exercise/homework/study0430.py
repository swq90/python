s1=71
s2=85
print("小明的成绩提高了%.2f%%"%(s2/s1))
s3=s2#s3指向s2所存储值的位置
s2=90#改变了s2的指向
print(s2,s3)#对s2赋值不影响s3
print(r'''hello,\n
world''')# r 表示str默认不转义，输入即输出；
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]#list可以嵌套list，形成矩阵
for y in L:#循环y为变量，取L中元素，记得写：
    print (y)
# 打印Apple:
print(L[0][0])#坐标从0开始
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
L.append("tt")#末尾添加#
L.insert(1,"88")#指定位置插入
#Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号
tu=(1)#数
print(tu)
tu=(1,)
print(tu)#元组
T=(1,2,L)#tuple可以嵌list，tuple不可以改变，但是list可以
print (L)
print(T)
L.pop(1)#删除指定位置
print (L)
print(T)
print(len(T))
ss=list(range(10))
print(ss)
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print("hello,%s!"%x)
n = 0
while n < 100:
    n = n + 1
    if n>10:
        break#循环终止
    if n%2==0:
        continue#跳出本次循环，break continue必须配合if使用
    print(n)
print("end")
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}#字典，key value 存储
print(d["Bob"])
s="tomas" in d
print(s)
print(d.get("bob","oh my god"))
s=set([1,2,3])#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#要创建一个set，需要提供一个list作为输入集合：
print(s)#set是无序的
s=set([1,2,1,4,2,1,2,3])
print(s)
s.add(7)
print(s)
s.remove(3)
print(s)
#使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。
#tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
#key 不能重复，list是变量，无法保证key是否重复
d={1,2,3}
print(d)
s=set([1,[2,9]])
print("set",s)

#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
#height=1.75
#weight=80
height = input("input your height")
weight = input("input your weight")
height=float(height)#input 返回str，要转换为int orfloat 才可以运损
weight=float(weight)
print(height)
print(weight)
bmi = weight/height**2
print("%.2f"%bmi)#格式化输出，几个%后面接几个
if bmi<18.5:
    print("light")
elif bmi<25:
    print("normal")
elif bmi<28:
    print("over")
elif bmi<32:
    print("fat")
elif bmi>32:
    print("dangerous")





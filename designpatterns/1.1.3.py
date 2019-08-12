class Person:
     def __init__(self,name,age):
         self.name = name
         self.age = age
     def get_person(self,):
         return "<Person (%s,%s)>"%(self.name,self.age)

p=Person("Bob",32)
print("Type of Object:",type(p),"Memory Address:",id(p))

# 封装：（数据和方法的隐藏，python没有提供关键字，可以将函数or变量前加__前缀，访问变为私有

#多态
a = "Bob"
b = [1,2,3]
c = (4,5,6)
print (a[1],b[0],c[2])
#1.根据入参提供方法的不同，实现。2.不同类型使用相同接口

# 继承：允许多重继承
#抽象：
# 组合：
class A(object):
    def a1(self):
        print('a1')

class B(object):
    def b (self):
        print ('b')
        A().a1()

objectB = B()
objectB.b()

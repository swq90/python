class student(object):
    pass
s=student()
s.name='mike'
print(s.name)

def set_age(self,age):#定义一个函数作为实例方法
    self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s)#给实例绑定一个方法
#MethodType(),第一个参数时要绑定的方法，第二个参数是要绑定的对象，第三个参数为类名（可省略）
s.set_age(20)#调用实例方法
print(s.age)#测试结果成功
# s2=student()
# s2.set_age(21)
# print(s2.age)#测试失败，因为s2没有绑定方法
#student.set_age=MethodType(set_age,student)#可以用MethodType调用方法
student.set_age=set_age
s2=student()
s2.set_age(21)
print(s2.age)#测试成功，student类已经绑定方法，so，s2可以调用

#限定实例属性
#例：只允许student 添加 name 和 age 属性
class Student(object):
    __slots__ = ('name','age')#用tuple定义允许绑定的属性名称
s=Student()
s.name='Bob'
print(s.name)
#s.socre=99#'Student' object has no attribute 'socre'

class JuniorStudent(Student):
    pass
js=JuniorStudent()
js.name='Alen'
js.score=100
js.sex='f'
print(js.name,js.score,js.sex)#成功
#__slots__的限定只对当前类有效，对继承的子类无效



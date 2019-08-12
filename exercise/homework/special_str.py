#_
class student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):#美观，且容易看出实例内部重要数据
        return 'student object(name:%s)'%self.name
print(student('bob'))
#没有__str__方法，输出：
# <__main__.student object at 0x000001FE227FAC88>
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name=%s)' % self.name
#     __repr__ = __str__
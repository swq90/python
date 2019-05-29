class Student():
    name = 'bob'

    def __init__(self):
        self.age1 = 18
        self.name = "jane"
        print(self.name)
        Student.name = "Jack"
        print(Student.name)

    def b(self):
        Student.name = "cindy"
        self.age = 5


a = Student()
print(a.age1)
# a.b()
print(a.age)
print(Student.name)
# b = Student()
# print(b.name)
# print(a.name, a.age)
# print(Student.name)
# print(Student.__init__(b))
# a.name = 'amy'
# a.age = 20
# print(a.name, a.age)  # 实例会屏蔽同名属性，但不对类属性修改
# print(b.name,b.age)
# print(Student.name)
# Student.name = 'kiko'
# print(a.name)
# print(b.name)
# print(Student.name)
# del a.name
# print(a.name, a.age)  # 删除实例属性后，类属性恢复

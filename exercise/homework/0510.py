class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        self.count=self.count+1

# 测试:
if Student.count != 0:
    print('a测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('b测试失败!')
        print('b测试失败!',Student.count)


    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('c测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')





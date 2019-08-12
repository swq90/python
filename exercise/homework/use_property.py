#为了检查参数，可以在类里定义方法
class Student(object):
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')#如果引发后面不再执行
        if value < 0 or value >100:
            raise ValueError('score must be between0-100')
        self._score=value

    def get_score(self):
        return self._score

s = Student()
s.set_score(60) # ok!
print(s.get_score())
#s.set_score(9999)

#利用Python内置的@property装饰器把一个方法变成属性调用，实现上面的操作
class student(object):
    @property
    def score(self):#把getter方法变为属性加property装饰器，，装饰器又创造了socre.setter装饰器把setter方法变为属性
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')#如果引发后面不再执行
        if value < 0 or value >100:
            raise ValueError('score must be between0-100')
        self._score=value
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth=value
    @property
    def age(self):
        return 2019-self._birth

s=student()
s.birth=1990
print(s.age)

#单态，所有对象共享状态
class Borg:
    __shared_state = {"1":"2"}
    def __init__(self):
        self.x = 1
        self.__dict__=self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4
print('b',b)
print('b1',b1)
print('state b',b.__dict__)
print('state b1',b1.__dict__)
print('b1.x = ',b1.x)
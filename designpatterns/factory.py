#ABCMeta,特殊元类，用来生成类Abstract，
#简单工厂模式，允许接口创建对象，但是不会暴露对象的创建逻辑
from abc import ABCMeta,abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass
class Cat(Animal):
    def do_say(self):
        print('mm')
class Dog(Animal):
    def do_say(self):
        print('ww')

#类实例化延迟到子类
class ForestFactory(object):
    def make_sound(self,object_type):
        return eval(object_type)().do_say()


if __name__ == "__main__":
    ff=ForestFactory()
    animal = input('which animal')
    ff.make_sound(animal)
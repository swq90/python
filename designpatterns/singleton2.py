#单例模式中懒汉实例化：确保在实际需要时创建一个对象
class Singleton2(object):
    __instance = None
    def __init__(self):
        if not Singleton2.__instance:
            print("__init__method called..")
        else:
            print("Instance already created:",self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance=Singleton2()
        return  cls.__instance

s = Singleton2()#初始化，但未创建
print ("object created",Singleton2.getInstance())#创建对象
s1=Singleton2
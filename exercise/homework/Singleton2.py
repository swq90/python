class Singleton(object):
    __instance=None
    def __init__(self):
        if not Singleton.__instance:#实例没有被创建
            print('....')
        else:
            print('Instance already created:',self.getInstance())
    @classmethod    #添加后才符合单例模式，有些静态的感觉？
    def getInstance(cls):#创建对象
        if not cls.__instance:
            cls.__instance=Singleton()
        return cls.__instance

s=Singleton()#初始化，但未创建
print(s.getInstance())#使用时创建
s1=Singleton()#已创建



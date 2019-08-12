class Singleton (object):
    def __new__(cls):
        if not hasattr(cls,'instance'):#判断对象cls是否具有属性instance
            cls.instance=super(Singleton,cls).__new__(cls)
        return cls.instance

s=Singleton()
print('object created',s)
s1=Singleton()
print('object created',s1)
#单例模式，只允许类生成一个实例
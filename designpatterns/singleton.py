class Singleton (object):

    #重写__new__来覆盖以前的方法，控制对象的创建
    def __new__(cls):
        if not hasattr(cls,'instance'): #hasattr,判断对象是否有某个属性
            cls.instance=super(Singleton,cls).__new__(cls)
        return cls.instance

#创建一个实例
s = Singleton()
print("object created",s)

#再次创建依然与上面相同，是同一个实例对象
s1 = Singleton()
print("object created",s1)
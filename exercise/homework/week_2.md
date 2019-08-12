
#####模块
######基础
    模块：一个.py文件就称之为一个模块（Module）
    包：避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
    mycompany
    ├─ __init__.py#每一个包目录下都必须有
    ├─ abc.py
    └─ xyz.py
    模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。
    创建自己的模块时，要注意：
        模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
        模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。
######使用模块
    作用域
        正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等
        类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
        类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
        '''
        def _private_1(name):
            return 'Hello, %s' % name

        def _private_2(name):
            return 'Hi, %s' % name

        def greeting(name):
            if len(name) > 3:
                return _private_1(name)
             else:
                return _private_2(name)
        '''
        我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
        外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
    安装第三方模块
        通过包管理工具pip完成的。
            pip install Pillow#安装第三方库
           
*********
-----------------
#####面向对象编程OOP
    数据封装、继承、多态是面向对象的三大特点

######类和实例
    class Student(object):
        pass     
    
    class Student(object):#object表示从哪个类继承下来
        def __init__(self, name, score):#创建实例的时候，利用_init_把一些我们认为必须绑定的属性强制填写进去
            self.name = name
            self.score = score
        def print_score(self):#student实例本身就含有要print的数据没必要外部函数访问，直接定义内部访问函数，这样把内部数据“封装”
                              #这种封装成为类的方法
            print('%s: %s' % (self.name, self.score))

        def get_grade(self):#定义方法，第一个参数是self，其他与普通函数一致
            if self.score >= 90:
                return 'A'
            elif self.score >= 60:
                return 'B'
            else:
                return 'C'
     bart.name = 'Bart Simpson'#实例可以任意增加属性，增加name属性
######访问限制                          
    def __init__(self, name, score):#不让内部属性被外部访问，可以用__双下划线，就变私有变量
        self.__name = name
        self.__score = score
    def set_score(self, score):#如果想外部访问score就在类里定义set_score的方法
                                #定义方法可以对参数进行检查，避免传入无效参数
        self.__score = score
    
    在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
    以一个下划线开头的实例变量名，可以被访问，但是，请视为私有变量，不要随意访问   
    bart = Student('Bart Simpson', 59)
    bart.get_name()
    bart.__name = 'New Name' # 设置__name变量！实际是新增一个__name的属性，因为类里已经把__name解释为_Student__name
######继承和多态
    class Animal(object):
        def run(self):
            print("Animal is running……")
    clas Dog(Animal):
        pass
    dog=Dog()
    dog.run()   #子类继承了父类的全部功能
    class Cat(Animal):
        def run(self):#子类run()覆盖了父类，运行时调用子类run()多态
            print('Cat is running……') 
    
    a=Dog()
    isinstance(a,Animal)
    isinstance(a,Dog)
    都为真，但反过来不可以
    def run_twice(animal):
        animal.run()
        animal.run()
    a.run_twice()#传入dog的实例，则输出两遍dog is running
  
  “开闭”原则
    对扩展开放：允许新增子类
    对修改封闭：不需要修改依赖Animal类型的方法
  继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

鸭子类型？
######对象类型
    type() #返回对象类型，基本类型，变量指向的函数或者类
    isinstance()
    dir()#获取对象的所有属性和方法，返回一个包含str的list
    getattr(obj,'x')#获取属性x
    setattr(obj,'x')#设置一个属性x
    hasattr(obj,'x')#有属性x吗？
######实例属性和类属性
    定义了类属性，实例属性可以访问，如果实例和类有相同的属性名，实例属性会屏蔽类属性，删除实例属性后才会访问类属性
        
  
#####面向对象的高级编程
    除了封装继承和多态，还有许多高级特性，如：
        多重继承，定制类，元类
        
    __slots__=('','')限定类的实例能添加的属性
        只对当前类有效，对继承其的子类没有限定作用
    @property 把类的getter方法当作属性调用，同时创建一个setter的装饰器，把setter方法变为属性
        要属性为只读，只要@property一个getter函数即可
        应用在类定义中，简洁且保证对参数进行必要检查，减少出错
######多重继承
      细分下来类的层次很复杂，这是可以先定义主要类
       class aaa(class1,class2，，，)
       一个子类可以继承多个父类  
       为了更好看出继承关系，class2MixIn，class3Mixin
       复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类
######定制类
    __str__
    __iter__
    __getitem__
    __getattr__  
    更多定制方法：https://docs.python.org/3/reference/datamodel.html#special-method-names
######使用枚举类
    from enum import Enum,unique
    class classname(Enum):
    #Enum可以把一组相关的常量存储在一个类中，类不可变，成员可直接相互比较
    @unique装饰器可以帮助检查保证没有重复值
######使用元类
    type()可以返回对象类型，也可以创建新类型
    def fn（self，）#先定义函数
    classname=type('calssname',（object,)#继承的父类,单继承记住tuple的写法#，dict（函数名=类的方法名））
    
    metaclass 元类
    
    
    
#####错误调试测试
    bug是程序编写错误，必须修正
    用户输入错误，要先检查输入
    异常，无法在运行中预测的
    调试：跟着程序执行，查看变量值是否正确
######错误处理
    try...except...finally...的错误处理机制,
        except可以有多个，把所有可能出现的错误一网打尽，如果捕捉到，finally前语句不在执行，
        所有错误都是从BaseException类派生，常见的错误类型和继承关系：
            https://docs.python.org/3/library/exceptions.html#exception-hierarchy
        多层调用时，底层出错也可以被捕获
    调用栈
        出错时分析调用栈信息，帮助定位错误
    记录错误
        内置logging，
            程序打印完错误胡会继续执行并且正常退出
            还会把错误记录到日志文件
    抛出错误   
        raise
        reraise，except捕获后只是记录错误，raise抛出交给上一层处理
        
######调试
    1.直接把有问题的变量都print出来
    2.assert，代替print，启动python解释器可以用-O（大写字母o）来关闭assert，关闭状态相当于pass
    3.logging,不抛出错误，但是记录错误信息至文件
        import logging
        logging basicConfig(level=logging.DEBUG/INFO/WARNING/ERROR)指定等级后，低级的就不报错了，以此来控制哪一级别的输出
    4.Pdb
        以参数-m pdb 启动
        (pdb) n             #下一步
        (pdb) p 变量名      #来查看变量
        (pdb)  q          #结束
        pdb.set_trace()     #在可能出现错误的位置放置，即可设置一个断点，可以用p 命令查看变量，也可以用c继续执行
    5.IDE
   
######单元测试
    针对一个函数写出几组测试用例写在一个测试模块里，就是一个单元测试
    如果修改了代码原有单元测试不通过，则是修改与原有行为不一致，改代码 or 单元测试
    
    
   
######文档测试
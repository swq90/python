
######0531


For CPython， id(x) ==the object’s address in memory.

David Beazley 著有两本基于 Python 3 的书，其中对数据模型进行了详尽的介绍。一本是 《Python 参考手册（第 4 版）》 ，另一本是与 Brian K. Jones 合著的《Python Cookbook（第 3 版）中文版》
Martelli （http://stackoverflow.com/users/95810/alex-martelli

groupby()
s = ''.join(s1)
######
学习使用异或^,xor

#####python数据模型
    数据模型其实是对python框架的描述，它规范了语言自身构建模块的 接口，不限于序列，迭代器，函数，类，上下文管理器
    不管在那种框架下，都会花费大量时间去实现那些会被框架本身调用的方法
    解释器碰到特殊句法时，会使用特殊方法激活一些基本兑现该操作
    双下划线开结的方法——魔术方法
    特殊方法名支持实现以下语言结构并与之交互：
        迭代，集合类，属性访问，运算符重载，函数和方法的调用，对象的创建和销毁，字符串表示形式和格式化，管理上下文（with模块）
    
    

######

    collections.namedtuple,用以构建只有少数属性但是没有方法的对象
    random.choice，从一个序列中随机选出一个元素的函数from random import choice 
    for card in reversed(deck):  反向迭代
######
    然而如果是 Python 内置的类型，比如列表（list）、字符串（str）、字节序列 （bytearray）等，那么 CPython 会抄个近路，__len__ 实际上会直
    接返回 PyVarObject 里的 ob_size 属性。PyVarObject 是表示内存中长度可变的内置对象的 C 语言结构体。直接读取这个值比调用一个方法要快很多
    for i in x: 背后则是 x.__iter__() 方
    目的是在你自己的子类的 __init__ 方法中调用超类的构造器。？？？
    
    
    
####把函数视作对象
#####一等函数
    在运行时创建
    能赋值给变量或数据结构中的元素
    能作为参数传给函数
    能作为函数的返回结果
######高阶函数  
    接收函数为参数，或者返回结果为参数
    map（），
    sort（iteration，key=）可选参数key提供一个函数
    如使用不定量的参数调用函数，可以编写 fn(*args, **keywords)
    
######匿名函数 lambda    
    在参数列表中最适合使用匿名函
    除了作为参数传给高阶函数之外，Python 很少使用匿名函数
    
######可调用对象 
    用户定义的函数（def,lambda)，内置函数，内置方法，方法，类，类的实例
    生成器函数
    判断对象能否被调用，最安全的方法是调用内置的callable()
    >>> [callable(obj) for obj in (abs, str, 13)] 
    [True, True, False]

######用户定义的可调用类型    
    何 Python 对象都可以表现得像函数。为此，只需实现 实例方法 __call__。
    必须再内部维护一个状态 
######函数内省
    dir(函数)可以探知函数有哪些属性    
    __annotations__ dict 参数和返回值的注解
    __call__ methodwrapper实现 () 运算符；即可调用对象协议
    __closure__ tuple 函数闭包，即自由变量的绑定（通常是 None）
    __code__ code 编译成字节码的函数元数据和函数定义体
    __defaults__ tuple 形式参数的默认值
    __get__ methodwrapper
    实现只读描述符协议（参见第 20 章）
    __globals__ dict 函数所在模块中的全局变量
    __kwdefaults__ dict 仅限关键字形式参数的默认值
    __name__ str 函数名称
    __qualname__ str
    函数的限定名称，如 Random.choice（ 参阅PEP 3155，https://www.python.org/dev/peps/pep-3155/）
######从定位参数到仅限关键字参数
    定义仅限关键字参数，要把它放在有*的参数后面，如过没有，则直接用*
    def f(a,*,b)，b不一定有默认值，但是强制必须传入参数
    仅限关键字参数的默认值在__kwdefaults__属性中
    函数对象有__defaults__属性，值为一元组，用来保存定位参数和关键字参数的默认值
    __code__,存储参数的名称，自身也有很多属性
    
    inspect._empty表示没有默认值，因为None也是有效的默认值

######获取关于参数的信息
######函数注解
    leetcode
    注解不做任何处理，只是存储在函数的__annotations__属性中
######支持函数式编程的包
    operator：mul itemget ter attrgetter,(能读取lambda表达式
    ，itemgetter(1) 的作用与 lambda fields: fields[1] 
    functools:   reduce
    
    
    
    
    
    
    
    
    
    
    
#####属性描述符
    描述符是实现了特定协议的类，这个协议包括 __get__、__set__ 和 __delete__ 方 法。property 类实现了完整的描述符协议。通常，可以只实现部分协议。其实，我们在 真实的代码中见到的大多数描述符只实现了 __get__ 和 __set__ 方法，还有很多只实现 了其中的一个。
    描述符是 Python 的独有特征，不仅在应用层中使用，在语言的基础设施中也有用到。除 了特性之外，使用描述符的 Python 功能还有方法及 classmethod 和 staticmethod 装饰 器。理解描述符是精通 Python 的关键。本章的话题就是描述符。
    
###17 使用期物处理并发
主要讨论 Python 3.2 引入的 concurrent.futures 模块
“期物”（future） 的概念。期物指一种对象，表示异步执行的操作。是 concurrent.futures 模块和 asyncio 包（第 18 章讨论）的基 础。


导入 requests 库。这个库不在标准库中，因此依照惯例，在导入标准库中的模块 （os、time 和 sys）之后导入，而且使用一个空行分隔开。
使用 futures.ThreadPoolExecutor 类实现多线程 下载的脚本

from concurrent import futures
```
def download_many(cc_list):    workers = min(MAX_WORKERS, len(cc_list))  ➍    with futures.ThreadPoolExecutor(workers) as executor:  ➎        res = executor.map(download_one, sorted(cc_list))
```
        
###asyncio 包处理并发
并发是指一次处理多件事。 并行是指一次做多件事。

    
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
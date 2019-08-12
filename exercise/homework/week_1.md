####PYTHON 学习笔记 01
######用数据类型
    1.整数，浮点数，字符串，布尔值TRUE FALSE，空值 None
        转译需要转译字符“\”
        也可用 r''表示''内部默认不转义
        ''',,,'''表示多行内容
    2.变量 常量
    3.字符编码
        ASCII,Unicode,UTF-8  
        ord()<->char()
    4.格式化输出
        ('hi,%s,you have $%d'%(Bob,1000))
        ("{0},{1}".format("str",int)
    5.list[] :L.append/pop/insert
            len(L)
      tuple{} ：初始化后不可修改（指向不变），只有一个元素用(a,)
      list 可作 tuple 的元素，tuple不变 变 可变
    6.dict {'key',value}
        一个key对应一个value，多个key会被最后的覆盖
        判断key是否存在
            "key" in dict：true or false
            dict.get('key')不存在返回None
            dict.get('key',-1)不存在返回指定值
        dict.pop()删除key同时删除对应value
      set=set[list]
        只存储key，不能重复创建一个set需要一个list作为输入集合
        set.add/remove,可重复加key，没效果，
        两个set可以进行，交集，并集的运算
###### 条件判断、循环
    1.if 判断语句：
      else：      
      if 判断语句：
      elif：
      ……
      elif：

    2.循环
        a) for……in list/tuple,把list or tuple的元素依次迭代出来
        b) while 满足循环，不满足跳出
        break：提前结束循环
        continue：跳出本轮，执行下一轮循环
    【注】
    input（）返回的时str，应注意转变类型s
    不可变对象：str不可变，list可变
        replace（）并不能改变str而是创建并返回一个新的str
######函数
    1.数据类型转换
        int(),float(),str(),bool()
    2.空函数
        def nop():
            pass     #占位符
    3.返回多个值
        return x,y
        多个值本质是个tuple
    return 返回函数结果，没有return自动返回 return none
    4.参数
        默认参数：参数名=默认值，不适用默认时传参要带参数名
        可变参数：传入参数个数是可变的，接收 tuple
                    def f（numbers）：
                    调用时 f（*L）
                    调用时先组装一个list or tuple，加*
        关键字参数：**kw，接收dict
        命名关键字参数 def f（name，job,*,city,age)
            限定关键子参数范围
        参数可自由组合
    5.递归函数
        优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出
        解决递归调用栈溢出的方法是通过尾递归优化
        在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
     
   ######高级特性
    1.切片 slice
        针对list tuple
        L[1,3],L[-2,-1],L[:10],L[-10:],L[10:20],
        L[:10:2],L[::5]
    2.迭代 iteration
        from collections import Iterable
        isinstance('abc', Iterable) # str是否可迭代
        for循环可实现类似下标循环
            for i,value in L(['a','b','c'])
            print (i,value)
            0 'a'
            1 'b'
            2 'c'
         
    3.列表生成器List Comprehensions
        [x * x for x in range(1, 11) if x % 2 == 0]
         [m + n for m in 'ABC' for n in 'XYZ']
    
    4.生成器 generator
        构造方法1，将列表生成器[]变为（）
        构造方法2，利用函数构造，必有 yield，遇到返回，再次执行时从yield语句处开始
        可用next(g)，每次使用调用一个元素，没有元素时，抛出StopIteration的错误。
        
    5.迭代器 iterator
        可以直接作用于for循环的数据类型有以下几种：
        a)集合数据类型：list、tuple、dict、set、str等；
        b)generator，生成器和带yield的generator function
        这两类可以直接for循环的对象统称为可迭代对象：Iterable
        可用isinstance()判断一个对象是否是Iterable对象
        集合数据类型：list、dict、str等是可迭代的Iterable但不是Iterator，
        可以通过iter()得到Iterator对象

【注意】
    杨辉三角的作业中，输出正确，存储的results有误，results指向的位置在生成器执行操作时数据发生变化受到影响，
    解决方法：利用for复制L作为返回值
   
#####函数式编程 Functional Programming
    抽象程度很高的编程范式，纯粹的函数式编程没有变量
    允许函数本身作为参数传入另一个函数，也接受返回一个函数
    Python允许变量，不是纯函数式编程
######高阶函数
    变量可以指向函数
    函数名也可以是变量（会引起错误，要恢复重启python
    把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式
    
    map() 两个参数，（函数，Iterable）
    map 把函数依次作用到序列，并返回新的Iterable
    reduce()两个参数，（函数，[x1,x2,x3,,])
    函数需接收两个参数把运算结果和下个元素做计算
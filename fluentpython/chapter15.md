#####if语句之外的else块
    for/else:
        for完毕时（没有被break中止）运行else
    while/else：
        循环条件为假而退出时运行else
    try/else:
        try块中没有异常抛出时运行else
        else自居抛出的异常不会有前面的except子句处理
        
    return break continue 或异常引控制权跳出，else子句也会被跳过
    
    总之，else在前面正常执行后执行，任何意外的跳出都会导致else子句的跳出
    
    
    try/except不仅用于处理错误，还用于控制流程
        EAFP  easier to ask for forgives than permission
            先假定存在有效的健或属性，当假设不成立，则捕获异常
    
    
        LBYL look before you leap
            在调用函数或查找属性或键之前显示测试前提条件， 代码中有许多if语句


#####上下文管理器和with模块
    上下文管理器对象存在的目的时管理with语句，就像迭代器的存在是为了管理for语句一样
    with语句目的，简化try/finally模式，保证一段代码运行完毕后执行某项操作，
        即便那段代码由于异常、return 语句或 sys.exit() 调用而中止，也会执行 指定的操作
        
        with 后面表达式得到的结果时上下文管理器对象，不过将其绑定到目标变量（as子句）
        是在上下文管理器对象上 调用__enter__方法的结果
    
    with不仅能管理资源，还能用于去掉常规的设置和清理代码，或者在另一个过程前后执行操作
    
    [::-1],反转    
    
    
    
    
######contextlib模块的实用工具
    redirect_stdout
    
    closing
        对象提供了close()方法，但是没有实现__enter/__exit__协议
     
    suppress
        构建临时忽略指定异常的上下文管理器
    @contextmanager
        减少创建上下文管理器的样板代码量，不用编写要给完整的类，定义__enter__,__exit__,
        只需实现一个yield语句的生成器，生成想让enter方法返回的值
        
    ContextDecorator
    
    Exitstack
        能进入多个上下文管理器
    

#####协程
    inspect.getgeneratorstate()确定协程当前状态
    
        GEN_CREATED,GEN_RUNNING,_GEN_SUSPENDED,GEN_CLOSED
        等待开始执行，解释器正在执行，在yield表达式处暂停，执行结束
        
        
    协程在yield处暂停，赋值语句中 = 右边的代码在赋值前执行，理解以后异步编程
    
    next(……)      预激协程，prime
    …….send(***)  多次调用
    预激活协程的装饰器
    
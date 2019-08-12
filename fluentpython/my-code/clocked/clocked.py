import time
def clock(func):
    def clocked(*args):
        t0=time.perf_counter()
        result = func(*args)#clocked的闭包中有自由变量fuc
        elapsed =time.perf_counter()-t0
        name =func.__name__
        arg_str = ','.join(repr(arg)for arg in args)
        print()
        return result
    return clocked#返回函数内部，取代被装饰的函数
def foo(s):
    n=int(s)
    if n==0:
        raise ('invalid value %s'%s)
    return 10/n
def bar():
    try:
        foo('0')
    except ValueError as e:#捕获错误，却不知如何处理
        print('value error')
        raise#上抛，不带参数则原样抛出
bar()

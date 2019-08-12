class fooError(ValueError):#选好继承关系，
    pass
def foo(s):
    n=int(s)
    if n==0:
        raise fooError('invalid value:%s:'%s)
    return 10/n
foo('0')

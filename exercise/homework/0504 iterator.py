for x in [1,2,3,4,5]:
    pass
it=iter([1,2,3,4,5])#迭代器
while 1:
    try:
        x=next(it)
    except StopIteration:
    break
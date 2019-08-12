' a test module '
__author__ = 'Jane'#把作者写进去

import sys#sys模块

def test():
    args = sys.argv#argv变量 用list存储了命令行所有参数，argv的第一个参数永远时该函数.py的函数名，so至少一个元素
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
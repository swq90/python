import os
print(os.name)
print(os.environ)
print(os.environ.get('PATH'))
print('绝对路径',os.path.abspath('.'))   #当前目录绝对路径,为什么要加 '.'
os.path.join('/users/wqsha','testdir')
os.mkdir('/User/wqsha','testdir')
from io import StringIO
f=StringIO()
f.write('hhhhhh')
f.write('aaaaa')
print(f.getvalue())#getvalue获得写入后的字符串
#要读取stringio要先用一个str初始化
f=StringIO('hi!\nit\'s me!\n')
n=1
while n<3 :
    s=f.readline()
    print(s)
    # print(s.strip())#去掉换行
    print(n)
    n=n+1

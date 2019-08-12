# f = open('C:\Users\wqsha\Desktop\test.txt', 'r')
try:
    f = open(r'C:\Users\wqsha\Desktop\test2.txt', 'r')#\是转义符，前面要加r，尝试，报错
    #只读取UTF-8编码的文本文件
    print(f.read())
finally:
    if f:
        f.close()

try:
    f = open(r'C:\Users\wqsha\Desktop\test.txt', 'r',encoding='ANSI')
    print(f.read())
finally:
    if f:
        f.close()

# for line in f.readlines():
#     print(line.strip())#把末尾的'\n'删掉
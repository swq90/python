#获取文件名列表,搜索.md文件

#搜索关键字是否在符合的要求的列表中

import os,sys
import time
l = [] #记录文件名
r = []
def filename(file_dir):
    # for root,dirs,files in os.walk(file_dir):
    # 当前目录路径,当前路径下所有子目录,当前目录下所有非目录子文件
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.md':
                l.append(os.path.join(root,file).replace('\\','/'))

    #os.path.splitext()将路径拆分为文件名和后缀

def searchfile(keys):
    for file in l:
        with open(file,'r',encoding='UTF-8') as f:
            rownum = 0
            for line in f.readlines():
                rownum += 1
                if keys in line:
                    r.append((file,rownum))
    print(r)


if __name__ == '__main__':
    file_dir = input('the dir of the file：')
    keys = input("the keys you want to search：")
    file_dir, keys = sys.argv()
    print(file_dir,keys)
    t0 = time.time()
    filename(file_dir)
    searchfile(keys)
    t1 = time.time()
    print(t1-t0)
#获取文件名列表,搜索.md文件

#搜索关键字是否在符合的要求的列表中

import os
# import time
from concurrent import futures

max_works = 10#最多使用几个线程
l = [] #记录文件名
r = []#结果


def filename(file_dir):
    # for root,dirs,files in os.walk(file_dir):
    # 当前目录路径,当前路径下所有子目录,当前目录下所有非目录子文件
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.md' or os.path.splitext(file)[1] == '.py':
                l.append(os.path.join(root,file).replace('\\','/'))

    # os.path.splitext()将路径拆分为文件名和后缀

def search_one(file):
    #
    with open(file, 'r', encoding='UTF-8') as f:
        rownum = 0
        t = []
        for line in f.readlines():
            rownum += 1
            if keys in line:
                t.append(rownum)
        if t:
            r.append({file:t})


def search_many(keys):
    workers = min(max_works,len(l))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(search_one,sorted(l))

    return len(list(res))

def main(search_many):

    file_dir = input('the dir of the file：')
    global keys
    keys = input("the keys you want to search：")
    filename(file_dir)
    search_many(keys)
    for i in r:
        print(i,'\n')

if __name__ == '__main__':
    main(search_many)
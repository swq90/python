import os.path
# import struct
import threading

# from concurrent import futures
from socket import socket,AF_INET,SOCK_STREAM


def main ():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('10.0.0.10', 666))
    print('等待连接...')
    server.listen(5)
    while True:
        conn, addr = server.accept()
        conn.settimeout()
        print("即将接收来自",addr,"的文件")

        t = threading.Thread(target=recv_file,args=(conn,addr))
        t.start()
    # with futures.ThreadPoolExecutor(max_workers=5) as executor:
    #     print('a')
    #     res = executor.submit(recv_file,(conn,addr))
    #     print('b')


def recv_file(conn, addr):
    file_path = os.getcwd()
    print(file_path)
    with conn:
        file_name = str(conn.recv(1024),encoding='utf8')
        print(file_name)
        while True:
            data = conn.recv(4096)
            with open(file_path+'/'+file_name, 'ab+')as fp:
                fp.write(data)
            print(file_path + '/' + file_name,'下载完成')
            if not data:
                break
    conn.close()
    return


if __name__ == '__main__':
    main()